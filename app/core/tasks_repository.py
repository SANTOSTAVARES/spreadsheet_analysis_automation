from app.models.tasks import Task
from app.config.database import session
from sqlalchemy import select


def get_task_by_task_id(task_id: int) -> Task:
    with session as s:
        stmt = s.execute(select(Task).where(Task.task_id == task_id))
        return stmt.scalars()


def get_first_task_in_db() -> Task:
    with session as s:
        stmt = s.execute(select(Task))
        return stmt.scalar()
