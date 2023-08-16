from ..fixtures.tasks_fixtures import insert_tasks_with_both_status_into_db, insert_task_weekdays_into_db
from ..fixtures.sheets_fixtures import insert_into_users_sheets_table, insert_sheet_into_db
from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file
from app.core.tasks_repository import get_task_by_task_id, get_first_task_in_db, get_true_taskweekdays_by_day, get_tasks_with_true_status_in_db


def test_get_task_by_task_id(insert_tasks_with_both_status_into_db):
    tasks_inserted_in_db = insert_tasks_with_both_status_into_db
    task_id = get_first_task_in_db().sheet_id

    # Check if there is task into db.
    assert tasks_inserted_in_db[0].sheet_id == task_id


def test_get_tasks_with_true_status(insert_tasks_with_both_status_into_db):
    true_tasks = get_tasks_with_true_status_in_db()

    # Check if it is true, the task_status from the first result.
    assert true_tasks[0][0].task_status == True

    # Check if it is true, the task_status from the second result.
    assert true_tasks[1][0].task_status == True
