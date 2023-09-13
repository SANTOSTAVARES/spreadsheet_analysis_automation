from app.queries.routine_repository import get_all_tasks_have_to_be_done_now
from app.services.sheets import Smartsheet


def do_tasks():

    tasks = get_all_tasks_have_to_be_done_now()
    for t in tasks:
        df = Smartsheet(sheet_id=t[0].sheet_name).get_sheet_as_dataframe()
