from app.domain.routine import do_tasks
from tests.fixtures.real_user_and_sheet_fixtures import insert_real_user_and_sheet_into_db


def test_routine(insert_real_user_and_sheet_into_db):
    real_user_and_sheet = insert_real_user_and_sheet_into_db
    do_tasks()
