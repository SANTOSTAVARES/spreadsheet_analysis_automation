from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file


def test_insert_user_into_db(insert_users_into_db):

    df = insert_users_into_db
    assert 'joao' == df['name'].loc[df.index[0]]
