from Functions import process_insert_db_and_save_csv

if __name__ == '__main__':
    file_path_demo = input('Provide path to the raw file as a string: ')
    db_path_demo = input('Provide the DB address as a string: ')
    table_name_demo = input('Provide the table name for the changed DB as a string: ')
    output_file_demo = input('Provide the new file name in the pattern (str.extension): ')
    export_data_to_DB_demo = input('Provide True or False to insert data into the TABLE: ')
    if export_data_to_DB_demo.lower() == 'true':
        export_data_to_DB_demo = True
    elif export_data_to_DB_demo.lower() == 'false':
        export_data_to_DB_demo = False
    process_insert_db_and_save_csv(file_path_demo, db_path_demo,
                                   table_name_demo, output_file_demo,
                                   export_data_to_DB= export_data_to_DB_demo)