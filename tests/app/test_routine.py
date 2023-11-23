from app.domain.routine import analyze_sheet_and_record_cheking_into_db
from tests.fixtures.real_user_and_sheet_fixtures import insert_real_user_and_sheet_into_db


def test_routine(insert_real_user_and_sheet_into_db):
    real_user_and_sheet = insert_real_user_and_sheet_into_db
    analyze_sheet_and_record_cheking_into_db()
