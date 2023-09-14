from datetime import datetime
from app.models.tasks import Task, TaskRuntime, TaskWeekday
from app.config.database import session
from sqlalchemy import select
from app.services.daily_checking import attribute_from_taksweekday_about_current_day


def get_all_tasks_have_to_be_done_now():
    time_now = datetime.now().time()
    current_day_on_taskweekday_object = attribute_from_taksweekday_about_current_day()

    with session as s:
        stmt = s.execute(
            select(Task)
            .join(TaskWeekday, TaskWeekday.task_id == Task.task_id)
            .join(TaskRuntime, TaskRuntime.task_id == Task.task_id)
            .where(
                (Task.task_status == True)
                &
                (current_day_on_taskweekday_object == True)
                &
                (TaskRuntime.runtime < time_now)
            )
        ).all()
        return stmt
