from ..fixtures.tasks_fixtures import insert_tasks_with_both_status_into_db
from ..fixtures.sheets_fixtures import insert_into_users_sheets_table, insert_sheet_into_db
from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file
from app.core.tasks_repository import get_task_by_task_id, get_first_task_in_db
from datetime import datetime


def test_get_task_by_task_id(insert_tasks_with_both_status_into_db):
    tasks_inserted_in_db = insert_tasks_with_both_status_into_db
    task_id = get_first_task_in_db().sheet_id

    # Check if there is task into db.
    assert tasks_inserted_in_db[0].sheet_id == task_id
