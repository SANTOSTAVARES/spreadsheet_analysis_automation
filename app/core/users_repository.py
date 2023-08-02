from app.models.user import User
from app.config.database import session
from sqlalchemy import select


def get_all_users() -> list[User]:
    with session as s:
        stmt = s.execute(select(User))
        return stmt.scalars().all()


def get_user_by_email(email: str) -> User:
    with session as s:
        stmt = s.execute(select(User).where(User.email == email))
        return stmt.scalar()
