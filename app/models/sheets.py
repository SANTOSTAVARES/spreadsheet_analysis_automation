import sqlalchemy as sa
from ..config.database import Base


class Sheet(Base):
    __tablename__ = 'sheets'

    sheet_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    identification_name: str = sa.Column(
        sa.String, nullable=False, index=True, unique=True)


class UserSheet(Base):
    __tablename__ = 'users_sheets'

    users_sheets_id: int = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True)
    user_id: int = sa.Column(sa.ForeignKey(
        "users.user_id", ondelete="CASCADE"), index=True)
    sheet_id: int = sa.Column(sa.ForeignKey(
        "sheets.sheet_id", ondelete="CASCADE"), index=True)
