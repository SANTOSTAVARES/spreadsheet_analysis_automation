from datetime import date
from ..fixtures.tasks_fixtures import (insert_tasks_with_both_status_into_db, insert_task_weekdays_into_db, insert_achieved_task_into_db,
                                       insert_users_tasks_into_db, insert_tasks_runtime_into_db)
from app.queries.tasks_repository import (get_tasks_with_true_status_in_db, get_taskweekday_by_current_day,
                                          get_users_tasks_by_task_id, get_tasks_runtime_by_task_id, get_achieved_task_by_tasks_runtime_id,
                                          get_achieved_task_by_tasks_runtime_id_and_created_at)
from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file


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


def test_get_users_tasks_by_task_id(insert_users_tasks_into_db):
    users_tasks_in_db = insert_users_tasks_into_db
    gotten_users_tasks_in_db = get_users_tasks_by_task_id(
        task_id=users_tasks_in_db[0].task_id)

    # Check if there is user_task in db.
    assert users_tasks_in_db[0].task_id == gotten_users_tasks_in_db[0][0].task_id


def test_get_task_runtime_by_task_id(insert_tasks_runtime_into_db):
    tasks_runtime = insert_tasks_runtime_into_db
    gotten_tasks_runtime_from_db = get_tasks_runtime_by_task_id(
        task_id=tasks_runtime[0].task_id)

    # Check if there is task_runtime in db.
    assert tasks_runtime[0].task_id == gotten_tasks_runtime_from_db[0][0].task_id


def test_get_achieved_tasks_by_task_runtime_id(insert_achieved_task_into_db):
    achieved_task_inserted_into_db = insert_achieved_task_into_db
    gotten_achieved_task_from_db = get_achieved_task_by_tasks_runtime_id(
        tasks_runtime_id=achieved_task_inserted_into_db.tasks_runtime_id)

    # Check if there is achieved_task in db.
    assert achieved_task_inserted_into_db.tasks_runtime_id == gotten_achieved_task_from_db[
        0][0].tasks_runtime_id

    # Check if query return empty list, when nonexistent tasks_runtime_id is informed.
    nonexistent_achieved_task = get_achieved_task_by_tasks_runtime_id(
        tasks_runtime_id=9_999)
    assert len(nonexistent_achieved_task) == 0
