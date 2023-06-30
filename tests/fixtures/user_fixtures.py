import pytest
from app.models.user import User
from ...app.config.settings import session
from ...app.services.deal_with_csv import convert_csv_to_dataframe, convert_list_of_lists_to_csv

@pytest.fixture()
def insert_users_into_db_by_csv_file():

    users_to_create_csv = [  ['name', 'email', 'user_type']
                    ['joao', 'joao@company.com', 'admin'],
                    ['maria', 'maria@company.com', 'operacional'],
                    ['ana', 'ana@company.com', 'operacional']
                  ]

    convert_list_of_lists_to_csv(data_list=users_to_create_csv, filename='users', path_to_save='..\..\data_to_input')
    users_from_dataframe = convert_csv_to_dataframe(path_and_file_name='C:\\Users\\s1203595\OneDrive - Syngenta\Documents\\aplicacoes_e_codigos\\smartsheet\\app\\teste.csv')

    users_list = []
    for i in users_from_dataframe.iterrows():
        users_list.append(User(name=i[1][0], email=i[1][1], user_type=i[1][2]))
    
    session.add_all(users_list)

    yield users_list

    session.flush()
    session.close()