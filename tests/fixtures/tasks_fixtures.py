import pytest
from app.config.database import session
from app.models.tasks import Task, TaskWeekday
from .sheets_fixtures import insert_into_users_sheets_table


@pytest.fixture()
def insert_tasks_with_both_status_into_db(insert_into_users_sheets_table):
    user_sheet = insert_into_users_sheets_table
    tasks_to_insert_in_db = [
        {
            "task_status": True,
            "sheet_id": user_sheet.sheet_id,
            "task_type": "Type 1",
            "main_column": "Column 1",
            "auxiliary_column": "Column 2",
            "reference_values": "Values",
        },
        {
            "task_status": False,
            "sheet_id": user_sheet.sheet_id,
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

    yield tasks_list

    session.flush()
    session.close()


@pytest.fixture()
def insert_task_with_true_status_into_db(insert_into_users_sheets_table):
    user_sheet = insert_into_users_sheets_table
    task = Task(task_status=True,
                sheet_id=user_sheet.sheet_id,
                task_type="Type 1",
                main_column="First Column",
                auxiliary_column="Second Column",
                reference_values="values")
    session.add(task)

    yield task

    session.flush()
    session.close()


@pytest.fixture()
def insert_task_weekdays_into_db(insert_task_with_true_status_into_db):
    task = insert_task_with_true_status_into_db
    task_weekdays = TaskWeekday(sunday=True, monday=True, tuesday=True, wednesday=True,
                                thursday=True, friday=True, saturday=True, task_id=task.task_id)
    session.add(task_weekdays)

    yield task_weekdays

    session.flush()
    session.close()
