from app.queries.routine_repository import get_all_tasks_have_to_be_done_now
from tests.fixtures.tasks_fixtures import insert_tasks_runtime_into_db, insert_tasks_with_both_status_into_db, insert_users_tasks_into_db, insert_task_weekdays_into_db
from tests.fixtures.sheets_fixtures import insert_sheet_into_db
from tests.fixtures.user_fixtures import insert_users_into_db, create_csv_users_file


def test_routine______(insert_tasks_runtime_into_db, insert_users_tasks_into_db, insert_task_weekdays_into_db):
    t = get_all_tasks_have_to_be_done_now()
    breakpoint()
