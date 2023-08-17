from datetime import datetime
from app.models.tasks import Task, TaskWeekday
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


def get_tasks_with_true_status_in_db():
    with session as s:
        stmt = s.execute(select(Task).where(Task.task_status == True))
        return stmt.fetchall()


def get_taskweekday_by_current_day():
    current_day = datetime.now().strftime('%A').lower()
    with session as s:
        stmt = s.execute(select(TaskWeekday).where(
            f'TaskWeekday.{current_day}' == True))
        return stmt.fetchall()
