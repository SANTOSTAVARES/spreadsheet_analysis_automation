import sqlalchemy as sa
from ..config.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email: str = sa.Column(sa.String, nullable=False)
    name: str = sa.Column(sa.String, nullable=False)
    user_type: str = sa.Column(sa.String, nullable=False)
