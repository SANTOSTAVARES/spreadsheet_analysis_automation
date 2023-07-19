import csv
import os
from pandas import DataFrame, read_csv


def convert_list_of_lists_to_text_file(data_list: list, file_name: str, path_to_save: str) -> None:
    """The csv must have header."""
    with open(f'{path_to_save}\{file_name}', 'w', newline='', encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_list)

    return None


def delete_file_from_directory(file_name: str, path: str) -> None:

    if os.path.isfile(f'{path}{file_name}'):
        os.remove(f'{path}{file_name}')
    else:
        raise FileNotFoundError('File not found')

    return None
