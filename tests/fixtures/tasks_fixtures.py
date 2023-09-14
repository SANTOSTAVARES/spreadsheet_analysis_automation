from datetime import datetime, timedelta
import pytest
from app.config.database import session
from app.models.tasks import Task, TaskWeekday, AchievedTask, UserTask, TaskRuntime
from tests.fixtures.user_fixtures import insert_users_into_db


@pytest.fixture()
def insert_tasks_with_both_status_into_db():

    tasks_to_insert_in_db = [
        {
            "task_status": True,
            "sheet_name": "plan1",
            "task_type": "Type 1",
            "main_column": "Column 1",
            "auxiliary_column": "Column 2",
            "reference_values": "Values",
        },
        {
            "task_status": True,
            "sheet_name": "plan1",
            "task_type": "Type 1",
            "main_column": "Column 1",
            "auxiliary_column": "Column 2",
            "reference_values": "Values",
        },
        {
            "task_status": False,
            "sheet_name": "plan1",
            "task_type": "Type 1",
            "main_column": "Column 3",
            "auxiliary_column": "Column 4",
            "reference_values": "More values",
        },
    ]

    tasks_list = []
    for t in tasks_to_insert_in_db:
        task = Task(
            task_status=t["task_status"],
            sheet_name=t["sheet_name"],
            task_type=t["task_type"],
            main_column=t["main_column"],
            auxiliary_column=t["auxiliary_column"],
            reference_values=t["reference_values"]
        )
        tasks_list.append(task)
    session.add_all(tasks_list)
    session.commit()

    yield tasks_list

    for task in tasks_list:
        session.delete(task)

    session.commit()
    session.close()


@pytest.fixture()
def insert_task_weekdays_into_db(insert_tasks_with_both_status_into_db):
    tasks = insert_tasks_with_both_status_into_db
    tasks_weekdays = []

    for task in tasks:
        task_id = task.task_id
        tasks_weekdays.append(TaskWeekday(sunday=True, monday=True, tuesday=True,
                                          wednesday=True, thursday=True, friday=True, saturday=True, task_id=task_id))
    session.add_all(tasks_weekdays)
    session.commit()

    yield tasks_weekdays

    for task in tasks_weekdays:
        session.delete(task)

    session.commit()
    session.close()


@pytest.fixture()
def insert_users_tasks_into_db(insert_tasks_with_both_status_into_db, insert_users_into_db):
    tasks_in_db = insert_tasks_with_both_status_into_db
    users_in_db = insert_users_into_db
    users_tasks = []

    for user in users_in_db:
        for task in tasks_in_db:
            users_tasks.append(
                UserTask(user_id=user.user_id, task_id=task.task_id))

    session.add_all(users_tasks)
    session.commit()

    yield users_tasks

    for ut in users_tasks:
        session.delete(ut)
    session.commit()
    session.close()


@pytest.fixture()
def insert_tasks_runtime_into_db(insert_tasks_with_both_status_into_db):
    task_id = insert_tasks_with_both_status_into_db[0].task_id
    time_now = datetime.now()
    time_one_hour_ago = time_now - timedelta(hours=1)
    time_after_one_hour = time_now + timedelta(hours=1)

    tasks_runtime = [
        {"runtime": time_one_hour_ago, "task_id": task_id},
        {"runtime": time_after_one_hour, "task_id": task_id},
    ]
    tasks_runtime_list = []
    for tr in tasks_runtime:
        task_runtime = TaskRuntime(
            runtime=tr["runtime"], task_id=tr["task_id"])
        tasks_runtime_list.append(task_runtime)

    session.add_all(tasks_runtime_list)
    session.commit()

    yield tasks_runtime_list

    for t_k in tasks_runtime_list:
        session.delete(t_k)
    session.commit()
    session.close()


@pytest.fixture()
def insert_achieved_task_into_db(insert_tasks_runtime_into_db):
    tasks_runtime = insert_tasks_runtime_into_db
    achieved_task = AchievedTask(
        tasks_runtime_id=tasks_runtime[0].tasks_runtime_id)
    session.add(achieved_task)
    session.commit()

    yield achieved_task

    session.delete(achieved_task)
    session.commit()
    session.close()
