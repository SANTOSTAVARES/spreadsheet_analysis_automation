from app.config.database import session
from app.models.tasks import AchievedTask


def insert_achieved_task_into_db(tasks_runtime_id: int) -> AchievedTask:
    achieved_task = AchievedTask(
        tasks_runtime_id=tasks_runtime_id)

    session.add(achieved_task)
    session.commit()
    session.close()

    return achieved_task
