from datetime import date
from app.queries.routine_repository import get_all_tasks_have_to_be_done_now
from app.services.sheets import Smartsheet, DataChecking
from app.queries.tasks_repository import get_achieved_task_by_tasks_runtime_id_and_created_at
from app.services.email import send_email
from app.services.html import list_of_row_value_outside_rule_converted_to_html_table_lines


def do_tasks():

    tasks_to_be_done = get_all_tasks_have_to_be_done_now()
    for task in tasks_to_be_done:
        achieved_task = get_achieved_task_by_tasks_runtime_id_and_created_at(
            tasks_runtime_id=task["tasks_runtime_id"], created_at=date.today())

        if len(achieved_task) == 0:

            smartsheet = Smartsheet(
                sheet_id=task["sheet_name"])
            df = smartsheet.get_sheet_as_dataframe()

            data_checking = DataChecking(data_table=df,
                                         checking_type=task["task_type"],
                                         main_column=task["main_column"],
                                         auxiliary_column=task["auxiliary_column"],
                                         reference_values=task["reference_values"]
                                         )

            list_of_row_value_outside_rule_and_rule_description = data_checking.do_check()

            row_value_outside_rule_as_html = list_of_row_value_outside_rule_converted_to_html_table_lines(
                row_value_outside_rule=list_of_row_value_outside_rule_and_rule_description[0])

            # sheet_information = smartsheet.get_sheet_information_by_sheet_id()
            sheet_information = {"Permalink": "", "name": ""}

            if len(list_of_row_value_outside_rule_and_rule_description[0]) > 0:
                send_email(sheet_identification=task["sheet_name"],
                           sheet_information=sheet_information,
                           rule_description=list_of_row_value_outside_rule_and_rule_description[1],
                           main_column=task["main_column"],
                           row_value_outside_rule=row_value_outside_rule_as_html,
                           recipients_emails="")
            del df
        else:
            achieved_task.pop(0)
