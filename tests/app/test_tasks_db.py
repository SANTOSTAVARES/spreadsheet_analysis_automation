from ..fixtures.tasks_fixtures import insert_tasks_with_both_status_into_db, insert_task_weekdays_into_db, insert_achieved_task_into_db
from ..fixtures.sheets_fixtures import insert_sheet_into_db
from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file
from app.queries.tasks_repository import get_first_task_in_db, get_tasks_with_true_status_in_db, get_taskweekday_by_current_day, get_achieved_tasks_by_task_id, get_first_achieved_task_in_db


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
    inserted_taskweekday = insert_task_weekdays_into_db
    taskweekday_gotten_from_db = get_taskweekday_by_current_day()

    # Check if there are TaskWeekday from current day in db.
    assert inserted_taskweekday[0].task_weekday_id == taskweekday_gotten_from_db[0][0].task_weekday_id
    assert inserted_taskweekday[1].task_weekday_id == taskweekday_gotten_from_db[1][0].task_weekday_id
    assert inserted_taskweekday[2].task_weekday_id == taskweekday_gotten_from_db[2][0].task_weekday_id


def test_get_achieved_tasks_by_task_id(insert_achieved_task_into_db):
    inserted_achieved_task = insert_achieved_task_into_db
    first_achieved_task_in_db = get_first_achieved_task_in_db()
    gotten_achieved_tasks = get_achieved_tasks_by_task_id(
        task_id=first_achieved_task_in_db.task_id)

    # Check if there is AchievedTask in db.
    assert inserted_achieved_task.task_id == gotten_achieved_tasks[0][0].task_id
