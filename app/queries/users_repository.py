from sqlalchemy import select
from app.config.database import session
from app.models.user import User
from app.models.tasks import UserTask


def get_all_users() -> list[User]:
    with session as s:
        stmt = s.execute(select(User))
        return stmt.scalars().all()


def get_user_by_email(email: str) -> User:
    with session as s:
        stmt = s.execute(select(User).where(User.email == email))
        return stmt.scalar()


def get_users_by_task_id(task_id: int):
    with session as s:
        stmt = s.execute(select(User).join(UserTask, UserTask.user_id ==
                                           User.user_id).where(UserTask.task_id == task_id)).all()
    return stmt
