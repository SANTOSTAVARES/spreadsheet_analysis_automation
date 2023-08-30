from app.queries.sheets_repository import get_sheet_by_identification_name
from ..fixtures.user_fixtures import insert_users_into_db, create_csv_users_file
from app.queries.users_repository import get_user_by_email
from ..fixtures.sheets_fixtures import insert_sheet_into_db


def test_get_sheet_by_identification_name(insert_sheet_into_db):
    sheet_in_db = insert_sheet_into_db.identification_name
    query = get_sheet_by_identification_name(identification_name=sheet_in_db)

    # Check if there is sheet in db.
    assert sheet_in_db == query.identification_name
