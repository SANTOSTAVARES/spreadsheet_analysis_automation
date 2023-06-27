import sqlalchemy as sa
from ..config.database import Base

class Sheet(Base):
    __tablename__ = 'sheets'

    sheet_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    identification_name: str = sa.Column(sa.String, nullable=False)


class UserSheet(Base):
    __tablename__ = 'users_sheets'

    users_sheets_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id: int = sa.Column(sa.ForeignKey("users.user_id"))
    sheet_id: int = sa.Column(sa.ForeignKey("sheets.sheet_id"))