import pytest
from app.models.user import User
from ...app.services.deal_with_csv import convert_list_of_lists_to_csv, convert_csv_to_dataframe

@pytest.fixture
def insert_user_into_db_by_csv_file():

    users_data = [['joao', 'joao@company.com', 'admin'],
                  ['maria', 'maria@company.com', 'operacional'],
                  ['ana', 'ana@company.com', 'operacional']
                  ]

    convert_list_of_lists_to_csv(data_list=users_data, filename='users', path_to_save='..\..\data_to_input')
    convert_csv_to_dataframe(path_and_file_name='C:\Users\s1203595\OneDrive - Syngenta\Documents\aaplicacoes_e_codigos\smartsheet\data_to_input')
        