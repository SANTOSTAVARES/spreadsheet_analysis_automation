from datetime import datetime
from app.models.sheets import Sheet
from app.models.tasks import Task, TaskRuntime, TaskWeekday, AchievedTask
from app.config.database import session
from sqlalchemy import select
from app.services.routine import attribute_from_taksweekday_about_current_day


def get_sheet_by_identification_name(identification_name: str) -> Sheet:
    with session as s:
        stmt = s.execute(select(Sheet).where(
            Sheet.identification_name == identification_name))
        return stmt.scalar()


def get_all_tasks_have_to_be_done_now():
    time_now = datetime.now().time()
    current_day_on_taskweekday_object = attribute_from_taksweekday_about_current_day()

    with session as s:
        stmt = s.execute(select(TaskRuntime.runtime,
                                Task.task_type,
                                Sheet.identification_name,
                                Task.main_column,
                                Task.auxiliary_column,
                                Task.reference_values,
                                TaskRuntime.tasks_runtime_id)
                         .join(TaskWeekday, TaskWeekday.task_id == Task.task_id)
                         .join(TaskRuntime, TaskRuntime.task_id == Task.task_id)
                         .join(Sheet, Sheet.sheet_id == Task.sheet_id)
                         .where(
            (Task.task_status == True)
            &
            (current_day_on_taskweekday_object == True)
            &
            (TaskRuntime.runtime < time_now)
        ))
        return stmt.fetchall()
