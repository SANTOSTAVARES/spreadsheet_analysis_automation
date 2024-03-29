import sqlalchemy as sa
from ..config.database import Base
from dataclasses import dataclass


@dataclass
class User(Base):
    __tablename__ = 'users'

    user_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email: str = sa.Column(sa.String, nullable=False, unique=True)
    name: str = sa.Column(sa.String, nullable=False)
    user_type: str = sa.Column(sa.String, nullable=False)
