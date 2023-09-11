from app.models.sheets import Sheet
from app.models.user import User
from app.models.tasks import Task, TaskRuntime, UserTask
from app.config.database import session
from sqlalchemy import select


def get_sheet_by_identification_name(identification_name: str) -> Sheet:
    with session as s:
        stmt = s.execute(select(Sheet).where(
            Sheet.identification_name == identification_name))
        return stmt.scalar()


def teste_query():
    with session as s:
        stmt = s.execute(select(Task.main_column, TaskRuntime.runtime, Task.task_id)
                         .join(TaskRuntime, TaskRuntime.task_id == Task.task_id)
                         .join(Sheet, Sheet.sheet_id == Task.sheet_id)
                         .join(UserTask, UserTask.task_id == Task.task_id)
                         .where(Task.task_status == True))
        return stmt.fetchall()
