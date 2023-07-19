import pytest
from app.services.deal_with_csv import convert_list_of_lists_to_text_file, delete_file_from_directory, convert_csv_to_dataframe
from pandas import read_csv


@pytest.fixture()
def create_csv_users_file():

    users_to_create_csv = [['name', 'email', 'user_type'],
                           ['joao', 'joao@company.com', 'admin'],
                           ['maria', 'maria@company.com', 'operacional'],
                           ['ana', 'ana@company.com', 'operacional']
                           ]
    file_name = 'users.csv'
    csv_file_path = '.\\data_to_input'

    convert_list_of_lists_to_text_file(data_list=users_to_create_csv, file_name=file_name,
                                       path_to_save=csv_file_path)

    yield users_to_create_csv

    delete_file_from_directory(
        file_name=f'{file_name}', path=f'{csv_file_path}\\')


@pytest.fixture()
def insert_users_into_db(create_csv_users_file):
    create_csv_users_file
    file_name = 'users.csv'
    csv_file_path = '.\\data_to_input\\'
    read_csv(filepath_or_buffer=f'{csv_file_path}{file_name}', header=0)
