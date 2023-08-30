import pytest
from app.config.database import session
from app.models.tasks import Task, TaskWeekday, AchievedTask
from tests.fixtures.sheets_fixtures import insert_sheet_into_db


@pytest.fixture()
def insert_tasks_with_both_status_into_db(insert_sheet_into_db):
    sheet_id = insert_sheet_into_db.sheet_id
    tasks_to_insert_in_db = [
        {
            "task_status": True,
            "sheet_id": sheet_id,
            "task_type": "Type 1",
            "main_column": "Column 1",
            "auxiliary_column": "Column 2",
            "reference_values": "Values",
        },
        {
            "task_status": True,
            "sheet_id": sheet_id,
            "task_type": "Type 99",
            "main_column": "Column 1",
            "auxiliary_column": "Column 2",
            "reference_values": "Values",
        },
        {
            "task_status": False,
            "sheet_id": sheet_id,
            "task_type": "Type 2",
            "main_column": "Column 3",
            "auxiliary_column": "Column 4",
            "reference_values": "More values",
        },
    ]

    tasks_list = []
    for t in tasks_to_insert_in_db:
        task = Task(
            task_status=t["task_status"],
            sheet_id=t["sheet_id"],
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
def insert_achieved_task_into_db(insert_tasks_with_both_status_into_db):

    task_id = insert_tasks_with_both_status_into_db[0].task_id
    at = AchievedTask(task_id=task_id)
    session.add(at)
    session.commit()

    yield at

    session.delete(at)
    session.commit()
    session.close()
