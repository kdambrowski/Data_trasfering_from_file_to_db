import sqlite3
import pandas as pd
import re
import os
from Settings import db_column_name_list, change_col_name_bool, show_match_col

#  If you have problem with reading XLS files check version for
# pip install --upgrade pandas openpyxl


def reorder_columns(df):
    """
    Reorder columns in a DataFrame based on an existing check dictionary.
    This function takes a DataFrame and reorders its columns based on the 'existing' list
    obtained from the 'get_dict_column_to_check' function.
    Parameters:
    df (pandas.DataFrame): The input DataFrame that needs its columns reordered.
    Returns:
    pandas.DataFrame: A DataFrame with columns reordered based on the existing check.
    """
    exist_check = get_dict_column_to_check(df)
    return df[exist_check['existing']]


def get_dict_column_to_check(df):
    """
     Create a dictionary with existing and non-existing columns in a DataFrame.
     This function takes a DataFrame and compares its column names with a predefined list
     ('db_column_name_list'). It then creates a dictionary with two lists: 'existing' for
     columns that exist in both the DataFrame and the list, and 'not_existing' for columns
     that are not found in the DataFrame.
     Parameters:
     df (pandas.DataFrame): The input DataFrame.
     Returns:
     dict: A dictionary with 'existing' and 'not_existing' lists.
     """
    exist_dict = {'existing': [], 'not_existing': []}
    for column in df.columns.tolist():
        if column in db_column_name_list:
            exist_dict['existing'].append(column)
        else:
            exist_dict['not_existing'].append(column)
    return exist_dict


def insert_into_database(values, db_path, table_name, column_order):
    """
    Insert data into a SQLite database table.
    This function inserts data from a list of values into a specified table in a SQLite
    database. The order of columns in the table is defined by the 'column_order' list.
    Parameters:
    values (list of tuples): A list of tuples containing the data to be inserted.
    db_path (str): The path to the SQLite database file.
    table_name (str): The name of the table in the database.
    column_order (list of str): The order of columns in the table.
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executemany(f"INSERT INTO {table_name} ({', '.join(column_order)}) VALUES ({', '.join(['?'] * len(values[0]))})",
                    values)
    conn.commit()
    conn.close()


def save_to_csv(df, output_file):
    """
    Save a DataFrame to a CSV file.
    This function saves a DataFrame to a CSV file with the specified file name.
    Parameters:
    df (pandas.DataFrame): The DataFrame to be saved.
    output_file (str): The name of the output CSV file.
    """
    df.to_csv(output_file, index=False)


def column_name_change(df):
    """
    Rename columns in a DataFrame based on specific conditions.
    This function renames columns in a DataFrame based on certain conditions. It renames
    columns with 'ACTION' in their name (except 'ACTION_ID') to 'ACTION_NAME'. It also
    renames columns related to completion rates and view rates accordingly.
    Parameters:
    df (pandas.DataFrame): The DataFrame whose columns are to be renamed.
    """
    for column in df.columns:
        if 'ACTION' in column.upper() and column != 'ACTION_ID' and column in df.columns:
            df.rename(columns={column: 'ACTION_NAME'}, inplace=True)
        elif 'COMPLETE' in column.upper() and 'RATE' in column.upper() and column in df.columns:
            df.rename(columns={column: 'COMPLETE_VIEW_RATE'}, inplace=True)
        elif 'VIEW' in column.upper() and 'RATE' in column.upper() and column in df.columns:
            df.rename(columns={column: 'VIEW_RATE'}, inplace=True)
        elif any(df[column].apply(lambda x: re.match(r'\d{4}-\d{2}-\d{2}', str(x)))):
            df.rename(columns={column: 'DAY'}, inplace=True)


def data_preparation(df, change_col_name= change_col_name_bool):
    """
    Prepare data in a DataFrame for insertion into a database.
    This function prepares data in a DataFrame for insertion into a database by renaming
    columns and applying column_name_change.
    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    Returns:
    pandas.DataFrame: A DataFrame with prepared data.
    """
    col_list = df.columns.tolist()
    rep_list = [name.replace(' ', '_').upper() for name in col_list]
    updated_df = pd.DataFrame(data= df.values, columns= rep_list)
    if change_col_name:
        column_name_change(updated_df)
    return updated_df


def process_insert_db_and_save_csv(file_path, db_path, table_name, output_file,
                                   export_data_to_DB= True, show_match_col= show_match_col):
    """
    Process data from a file, prepare it, and optionally insert it into a database.
    This function reads data from a CSV or Excel file, prepares it using data_preparation,
    saves it to a CSV file, and optionally inserts it into a SQLite database table.
    Parameters:
    file_path (str): The path to the input file (CSV or Excel).
    db_path (str): The path to the SQLite database file.
    table_name (str): The name of the table in the database.
    output_file (str): The name of the output CSV file.
    export_data_to_DB (bool): Whether to export data to the database (default is True).
    """
    # The file path should point to a CSV or XLS OR XLSX file
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == '.csv':
        df = pd.read_csv(file_path)
    elif file_extension == '.xls' or file_extension == '.xlsx':
        df = pd.read_excel(file_path)
    # set df to match with SQL DB
    updated_df = data_preparation(df)
    # select only columns that match with DB columns
    dict_check = get_dict_column_to_check(updated_df)
    updated_df = reorder_columns(updated_df)
    # extract values from DF
    values = updated_df.values.tolist()
    # save prepared file
    save_to_csv(updated_df, output_file)
    print(f'File {output_file} has been saved successfully')
    # shows matching columns name between provided file and the DB
    if show_match_col:
        print(f'Column name: {dict_check["existing"]} matches to column name in the DB')
    # condition for change table in DB
    if export_data_to_DB:
        insert_into_database(values, db_path, table_name, dict_check['existing'])
        print(f"Data has been insert to columns {dict_check['existing']}")

