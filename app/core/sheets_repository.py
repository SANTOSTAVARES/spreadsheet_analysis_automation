from app.models.sheets import Sheet, UserSheet
from app.config.database import session
from sqlalchemy import select


def get_sheet_by_identification_name(identification_name: str) -> Sheet:
    with session as s:
        stmt = s.execute(select(Sheet).where(
            Sheet.identification_name == identification_name))
        return stmt.scalar()
