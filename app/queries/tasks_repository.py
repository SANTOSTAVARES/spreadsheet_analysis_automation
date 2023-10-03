from datetime import date
from sqlalchemy import select
from app.services.daily_checking import attribute_from_taksweekday_about_current_day
from app.config.database import session
from app.models.tasks import Task, TaskWeekday, AchievedTask, UserTask, TaskRuntime


def get_task_by_task_id(task_id: int) -> Task:
    with session as s:
        stmt = s.execute(select(Task).where(Task.task_id == task_id))
        return stmt.scalars()


def get_tasks_with_true_status_in_db():
    with session as s:
        stmt = s.execute(select(Task).where(Task.task_status == True))
        return stmt.fetchall()


def get_taskweekday_by_current_day():
    current_day = attribute_from_taksweekday_about_current_day()
    with session as s:
        stmt = s.execute(select(TaskWeekday).where(current_day == True))
        return stmt.fetchall()


def get_users_tasks_by_task_id(task_id: int):
    with session as s:
        stmt = s.execute(select(UserTask).where(
            UserTask.task_id == task_id))
        return stmt.fetchall()


def get_tasks_runtime_by_task_id(task_id: int):
    with session as s:
        stmt = s.execute(select(TaskRuntime).where(
            TaskRuntime.task_id == task_id))
        return stmt.fetchall()


def get_achieved_task_by_tasks_runtime_id(tasks_runtime_id: int):
    with session as s:
        stmt = s.execute(select(AchievedTask).where(
            AchievedTask.tasks_runtime_id == tasks_runtime_id))
        return stmt.fetchall()


def get_achieved_task_by_tasks_runtime_id_and_created_at(tasks_runtime_id: int, created_at: date):
    with session as s:
        stmt = s.execute(
            select(AchievedTask)
            .where(
                (AchievedTask.tasks_runtime_id == tasks_runtime_id)
                &
                (AchievedTask.created_at == created_at)
            )
        )
        return stmt.fetchall()


def get_all_tasks_runtime():
    with session as s:
        stmt = s.execute(select(TaskRuntime))
        return stmt.scalars().all()
