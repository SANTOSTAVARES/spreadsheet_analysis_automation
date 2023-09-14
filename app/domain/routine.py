from app.queries.routine_repository import get_all_tasks_have_to_be_done_now
from app.services.sheets import Smartsheet, DataChecking


def do_tasks():

    tasks = get_all_tasks_have_to_be_done_now()
    for t in tasks:

        task = DataChecking(data_table=Smartsheet(sheet_id=t[0].sheet_name).get_sheet_as_dataframe(),
                            checking_type=t[0].task_type,
                            main_column=t[0].main_column,
                            auxiliary_column=t[0].auxiliary_column,
                            reference_values=t[0].reference_values
                            ).do_check()
