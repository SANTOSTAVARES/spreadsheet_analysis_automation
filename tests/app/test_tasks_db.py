from datetime import datetime
from ..fixtures.tasks_fixtures import insert_tasks_with_both_status_into_db, insert_task_weekdays_into_db, insert_achievied_task_into_db
from ..fixtures.sheets_fixtures import insert_into_users_sheets_table, insert_sheet_into_db
from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file
from app.core.tasks_repository import get_first_task_in_db, get_tasks_with_true_status_in_db, get_taskweekday_by_current_day, get_achieved_tasks_by_task_id


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


def test_get_taskweekday_by_current_day(insert_task_weekdays_into_db):
    insert_task_weekdays_into_db
    inserted_taskweekday = insert_task_weekdays_into_db
    taskweekday_gotten_from_db = get_taskweekday_by_current_day()

    # Check if there is TaskWeekday in db
    assert inserted_taskweekday.task_weekday_id == taskweekday_gotten_from_db[
        0][0].task_weekday_id


def test_get_achieved_tasks_by_task_id(insert_achievied_task_into_db):
    inserted_achievied_task = insert_achievied_task_into_db
    ################################################################
    # Task_id está mockado.
    gotten_achieved_tasks = get_achieved_tasks_by_task_id(task_id=1)
    assert inserted_achievied_task.task_id == gotten_achieved_tasks[0][0].task_id
