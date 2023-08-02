import pytest
from app.config.database import session
from app.models.sheets import Sheet, UserSheet
from .user_fixtures import insert_users_into_db, create_csv_users_file
from app.core.users_repository import get_user_by_email


@pytest.fixture()
def insert_sheet_into_db():
    sheet = Sheet(identification_name="plan1")
    session.add(sheet)

    yield sheet

    session.flush()
    session.close()


@pytest.fixture()
def insert_into_users_sheets_table(insert_users_into_db, insert_sheet_into_db):
    sheet_id = insert_sheet_into_db
    df = insert_users_into_db
    user_email = df['email'].loc[df.index[0]]
    first_user_in_db = get_user_by_email(email=user_email)

    user_sheet = UserSheet(user_id=first_user_in_db.user_id,
                           sheet_id=sheet_id.sheet_id)
    session.add(user_sheet)

    yield user_sheet

    session.flush()
    session.close()
