from datetime import date
from app.config.database import session
from app.models.tasks import AchievedTask
from app.queries.users_repository import get_users_by_task_id
from app.queries.routine_repository import get_all_tasks_have_to_be_done_now
from app.queries.tasks_repository import get_achieved_task_by_tasks_runtime_id_and_created_at
from app.services.sheets import Smartsheet, DataChecking
from app.services.email import send_email
from app.services.html import list_of_row_value_outside_rule_converted_to_html_table_lines


def analyze_sheet_and_record_cheking_into_db():

    tasks_to_be_done = get_all_tasks_have_to_be_done_now()
    for task in tasks_to_be_done:
        achieved_task = get_achieved_task_by_tasks_runtime_id_and_created_at(
            tasks_runtime_id=task["tasks_runtime_id"],
            created_at=date.today())

        if len(achieved_task) == 0:
            DataChecking(sheet_id=task["sheet_name"],
                         sheet_identification=task["sheet_name"],
                         task_id=task["task_id"],
                         checking_type=task["task_type"],
                         main_column=task["main_column"],
                         auxiliary_column=task["auxiliary_column"],
                         reference_values=task["reference_values"]).do_checking_and_send_email()

            achieved_task = AchievedTask(
                tasks_runtime_id=task["tasks_runtime_id"])
            session.add(achieved_task)
            session.commit()
            return task
        else:
            achieved_task.pop(0)
