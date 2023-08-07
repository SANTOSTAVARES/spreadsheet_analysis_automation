from app.core.sheets_repository import get_sheet_by_identification_name
from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file
from app.core.users_repository import get_user_by_email
from ..fixtures.sheets_fixtures import insert_into_users_sheets_table, insert_sheet_into_db


def test_get_sheet_by_identification_name(insert_sheet_into_db):
    sheet_in_db = insert_sheet_into_db.identification_name
    query = get_sheet_by_identification_name(identification_name=sheet_in_db)

    # Check if there is sheet in db.
    assert sheet_in_db == query.identification_name


def test_insert_into_users_sheets_table(insert_into_users_sheets_table, insert_sheet_into_db):
    sheet = insert_sheet_into_db
    user_sheet = insert_into_users_sheets_table

    # Check if there is record into users_sheets table.
    assert user_sheet.sheet_id == sheet.sheet_id
