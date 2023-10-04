from datetime import datetime, timedelta
import pytest
from app.config.database import session
from app.models.user import User
from app.models.tasks import Task, UserTask, TaskWeekday, TaskRuntime
from app.queries.tasks_repository import get_all_tasks_runtime
from app.config.settings import setting


@pytest.fixture
def insert_real_user_and_sheet_into_db():

    real_user = User(email=setting.REAL_EMAIL,
                     name=setting.REAL_USER_NAME,
                     user_type="operacional")

    task = Task(task_status=True,
                sheet_name=setting.REAL_SHEET_NAME,
                task_type="03",
                main_column=setting.REAL_MAIN_COLUMN,
                auxiliary_column=None,
                reference_values="01|1000")

    session.add(real_user)
    session.add(task)
    session.commit()

    user_task = UserTask(user_id=real_user.user_id, task_id=task.task_id)

    task_weekdays = TaskWeekday(sunday=True, monday=True, tuesday=True, wednesday=True,
                                thursday=True, friday=True, saturday=True, task_id=task.task_id)

    task_runtime = TaskRuntime(runtime=(datetime.now() - timedelta(hours=2)),
                               task_id=task.task_id)

    data_to_input = [user_task, task_weekdays, task_runtime]
    for i in data_to_input:
        session.add(i)
    session.commit()
    session.close()

    yield

    session.delete(real_user)
    session.delete(task)
    session.commit()
    session.close()

    with session as s:
        session.query(TaskWeekday).filter(TaskWeekday.sunday ==
                                          True).delete(synchronize_session=False)

    with session as s:
        session.query(UserTask).filter(UserTask.task_id ==
                                       task.task_id).delete(synchronize_session=False)

    with session as s:
        session.query(TaskRuntime).filter(TaskRuntime.task_id ==
                                          task.task_id).delete(synchronize_session=False)
