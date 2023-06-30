from..fixtures.user_fixtures import insert_users_into_db_by_csv_file

def test_insert_user_into_db(insert_users_into_db_by_csv_file):
    # Assertion 1: Check if users are inserted into the database correctly
    users = insert_users_into_db_by_csv_file
    assert len(users) == 3  # Assuming there are three users in the CSV file

    # Assertion 2: Check if the first user has the correct name, email, and user type
    first_user = users[0]
    assert first_user.name == 'joao'
    assert first_user.email == 'joao@company.com'
    assert first_user.user_type == 'admin'

    # Assertion 3: Check if the second user has the correct name, email, and user type
    second_user = users[1]
    assert second_user.name == 'maria'
    assert second_user.email == 'maria@company.com'
    assert second_user.user_type == 'operacional'

    # Assertion 4: Check if the third user has the correct name, email, and user type
    third_user = users[2]
    assert third_user.name == 'ana'
    assert third_user.email == 'ana@company.com'
    assert third_user.user_type == 'operacional'