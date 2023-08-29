from dataclasses import dataclass
import sqlalchemy as sa
from ..config.database import Base


@dataclass
class Sheet(Base):
    __tablename__ = 'sheets'

    sheet_id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    identification_name: str = sa.Column(
        sa.String, nullable=False, index=True, unique=True)
