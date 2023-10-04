from datetime import date
from app.queries.routine_repository import get_all_tasks_have_to_be_done_now
from app.services.sheets import Smartsheet, DataChecking
from app.queries.tasks_repository import get_achieved_task_by_tasks_runtime_id_and_created_at


def do_tasks():

    tasks_to_be_done = get_all_tasks_have_to_be_done_now()
    for task in tasks_to_be_done:
        achieved_task = get_achieved_task_by_tasks_runtime_id_and_created_at(
            tasks_runtime_id=task["tasks_runtime_id"], created_at=date.today())

        if len(achieved_task) == 0:
            df = Smartsheet(
                sheet_id=task["sheet_name"]).get_sheet_as_dataframe()

            row_value_outside_rule = DataChecking(data_table=df,
                                                  checking_type=task["task_type"],
                                                  main_column=task["main_column"],
                                                  auxiliary_column=task["auxiliary_column"],
                                                  reference_values=task["reference_values"]
                                                  ).do_check()

        else:
            achieved_task.pop(0)
