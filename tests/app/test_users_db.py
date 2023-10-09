from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file
from ..fixtures.tasks_fixtures import insert_users_tasks_into_db, insert_tasks_with_both_status_into_db
from app.queries.users_repository import get_all_users, get_user_by_email
from app.queries.users_repository import get_users_by_task_id


def test_get_user_by_email(insert_users_into_db):
    user_email = insert_users_into_db[0].email
    first_user_in_db = get_user_by_email(email=user_email)

    # Check if there is available in db.
    assert user_email == first_user_in_db.email


def test_get_all_users(insert_users_into_db):

    users_inserted_in_db = insert_users_into_db
    users_in_db = get_all_users()

    # Check if there are users names available in databse.
    assert users_in_db[0].name == users_inserted_in_db[0].name
    assert users_in_db[1].name == users_inserted_in_db[1].name
    assert users_in_db[2].name == users_inserted_in_db[2].name

    # Check if there are users e-mails available in databse.
    assert users_in_db[0].email == users_inserted_in_db[0].email
    assert users_in_db[1].email == users_inserted_in_db[1].email
    assert users_in_db[2].email == users_inserted_in_db[2].email

    # Check if there are users type available in databse.
    assert users_in_db[0].user_type == users_inserted_in_db[0].user_type
    assert users_in_db[1].user_type == users_inserted_in_db[1].user_type
    assert users_in_db[2].user_type == users_inserted_in_db[2].user_type


def test_get_users_by_task_id(insert_users_tasks_into_db):
    user_task_inserted_in_db = insert_users_tasks_into_db

    user_gotten_from_db = get_users_by_task_id(
        task_id=user_task_inserted_in_db[0].task_id)
