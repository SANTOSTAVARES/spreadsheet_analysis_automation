from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file
from app.queries.users_repository import get_all_users, get_user_by_email


def test_get_user_by_email(insert_users_into_db):
    df = insert_users_into_db
    user_email = df['email'].loc[df.index[0]]
    first_user_in_db = get_user_by_email(email=user_email)

    # Check if there is available in db.
    assert user_email == first_user_in_db.email


def test_get_all_users(insert_users_into_db):

    df = insert_users_into_db
    users_in_db = get_all_users()

    # Check if there are users names available in databse
    assert users_in_db[0].name == df['name'].loc[df.index[0]]
    assert users_in_db[1].name == df['name'].loc[df.index[1]]
    assert users_in_db[2].name == df['name'].loc[df.index[2]]

    # Check if there are users e-mails available in databse
    assert users_in_db[0].email == df['email'].loc[df.index[0]]
    assert users_in_db[1].email == df['email'].loc[df.index[1]]
    assert users_in_db[2].email == df['email'].loc[df.index[2]]

    # Check if there are users type available in databse
    assert users_in_db[0].user_type == df['user_type'].loc[df.index[0]]
    assert users_in_db[1].user_type == df['user_type'].loc[df.index[1]]
    assert users_in_db[2].user_type == df['user_type'].loc[df.index[2]]
