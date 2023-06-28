import csv
from pandas import DataFrame, read_csv

def convert_list_of_lists_to_csv(data_list: list, filename: str, path_to_save: str) -> None:
    with open(f'{path_to_save}\{filename}.csv', 'w', newline='', encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_list)
    
    return None

def convert_csv_to_dataframe(path_and_file_name: str) -> DataFrame:
    
    return read_csv(path_and_file_name)
