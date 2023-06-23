import sqlalchemy as sa
from ...config.base import Base


class User(Base):
    __tablename__ = 'users'

    user_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email: str = sa.column(sa.String, primary_key=True, nullable=False)
    name: str = sa.column(sa.String, nullable=False)
    user_type: str = sa.column(sa.String, nullable=False)
