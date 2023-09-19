# Here set columns name from DS

db_column_name_list = ['DAY', 'NAME_OF_FILE', 'ACTION_NAME',
                       'ACTION_ID', 'SOURCE', 'CLICKS', 'UNIQUE_CLICKS',
                       'IMPRESSIONS', 'ITEM', 'VIEW_RATE', 'COMPLETE_VIEW_RATE',
                       'COST', 'ORDERS', 'FILE_RECEIVED', 'CHANNEL']

"""This is needed for the data_preparation function, where the change_col_name parameter determines 
whether the column names from the input file should be changed to match the column names in the provided database.
 
 If you want to match the column names that are not directly matched, please check the column_name_change
 and adjust it to your needs."""
change_col_name_bool = False
# value for function process_insert_db_and_save_csv
show_match_col = True
