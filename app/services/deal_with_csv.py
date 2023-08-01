import csv
import os
from pandas import DataFrame, read_csv
from dataclasses import dataclass
from app.models.user import User


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


@dataclass
class CsvData:

    file_name: str
    csv_file_path: str

    def convert_csv_to_users_list(self) -> list[User]:

        df = read_csv(f'{self.csv_file_path}{self.file_name}')

        users_list = []
        for i in df.iterrows():
            users_list.append(
                User(name=i[1][0], email=i[1][1], user_type=i[1][2]))

        return users_list
