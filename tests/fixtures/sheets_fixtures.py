import pytest
from app.config.database import session
from app.models.sheets import Sheet
from .user_fixtures import insert_users_into_db, create_csv_users_file
from app.queries.users_repository import get_user_by_email


@pytest.fixture()
def insert_sheet_into_db():
    sheet = Sheet(identification_name="plan1")
    session.add(sheet)
    session.commit()

    yield sheet

    session.delete(sheet)
    session.commit()
    session.close()
