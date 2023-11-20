from dataclasses import dataclass
import sys
from pandas.core.frame import DataFrame
import smartsheet
from smartsheet_dataframe import get_sheet_as_df
import win32com.client
from app.config.settings import setting
from app.queries.users_repository import get_users_by_task_id

sys.path.append('..\\config')
token = setting.SMARTSHEET_TOKEN


@dataclass
class Smartsheet:

    sheet_id: str | None
    user_token: str = token

    def get_bearer_authentication(self) -> dict:
        return {'Authorization': f'Bearer {self.user_token}'}

    def get_sheets_name_list(self) -> smartsheet.models.sheet.Sheet:
        smart = smartsheet.Smartsheet(access_token=self.user_token)
        return smart.Sheets.list_sheets(include_all=True).data

    def get_sheet_as_dataframe(self) -> DataFrame:

        try:
            df = get_sheet_as_df(token=self.user_token,
                                 sheet_id=self.sheet_id)
        except Exception as e:
            return e
        else:
            return df

    def get_sheet_information_by_sheet_id(self):
        sheets_name_list = self.get_sheets_name_list()
        sheet_information = {}
        for sheet in sheets_name_list:

            if str(sheet.id) == self.sheet_id:
                sheet_information["name"] = sheet.name
                sheet_information["permalink"] = sheet.permalink
                break
        del sheets_name_list
        return sheet_information


@dataclass
class DataChecking:

    sheet_id: str | None
    user_token: str = token
    sheet_identification: str
    # data_table: DataFrame
    task_id: int
    checking_type: str
    main_column: str
    auxiliary_column: str = None
    reference_values: str = None

    def get_bearer_authentication(self) -> dict:
        return {'Authorization': f'Bearer {self.user_token}'}

    def get_sheet_as_dataframe(self) -> DataFrame:

        try:
            df = get_sheet_as_df(token=self.user_token,
                                 sheet_id=self.sheet_id)
        except Exception as e:
            return e
        else:
            return df

    def get_sheets_name_list(self) -> smartsheet.models.sheet.Sheet:
        smart = smartsheet.Smartsheet(access_token=self.user_token)
        return smart.Sheets.list_sheets(include_all=True).data

    def get_sheet_information_by_sheet_id(self) -> dict:
        sheets_name_list = self.get_sheets_name_list()
        sheet_information = {}
        for sheet in sheets_name_list:

            if str(sheet.id) == self.sheet_id:
                sheet_information["name"] = sheet.name
                sheet_information["permalink"] = sheet.permalink
                break
        del sheets_name_list
        return sheet_information

    def emails_list(self) -> list:
        users = get_users_by_task_id(task_id=self.task_id)
        emails_list = [user[0].email for user in users]
        return emails_list

    def list_of_row_value_outside_rule_converted_to_html_table_lines(self) -> str:
        table_lines = ""
        for i in self.specify_checking():

            list_converted_to_html_table_lines = f"""<tr>
                <td>{i[0]}</td>
                <td>{i[1]}</td>
            </tr>"""

            table_lines += list_converted_to_html_table_lines

        return table_lines

    def send_email(self) -> None:

        recipients_emails_as_str = ""
        for email in self.emails_list():
            recipients_emails_as_str += email + "; "

        ol = win32com.client.Dispatch('Outlook.Application')
        olmailitem = 0x0
        newmail = ol.CreateItem(olmailitem)
        newmail.Subject = 'Validação automática de dados da Smartsheet'
        newmail.To = recipients_emails_as_str

        newmail.HTMLbody = (
            f""" <!DOCTYPE html>
            <html lang="pt-br">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>E-mail de validação de planilha da Smartsheet</title>
            </head>

            <style>
                table, th, td {{
                border:1px solid black;
                }}
            </style>
            
            <body>
                <p>Este é um e-mail automático, gerado por ter sido encontrado divergências em relação a regra para coluna e planilha descrita abaixo.</p>
                <p><b>ID: </b>{self.sheet_identification}</p>
                <p><b>Planilha: </b>{self.get_sheet_information_by_sheet_id["name"]}</p>
                <p><b>Coluna: </b>{self.main_column}</p>
                <p><b>Link: </b>{self.get_sheet_information_by_sheet_id["permalink"]}</p>
                <p><b>Regra de validação:</b> {self.specify_checking[1]}</p>

                <table>
                    <tr>
                        <th>Linha</th>
                        <th>Valor</th>
                    </tr>
                    {self.list_of_row_value_outside_rule_converted_to_html_table_lines()}         
                </table>
            </body>
            </html> 
        """
        )
        newmail.Send()
        return None

    def check_value_range_and_ignore_blank_cell(self) -> list:
        min_max_number = self.reference_values.split("|")
        min_number = int(min_max_number[0])
        max_number = int(min_max_number[1])
        row_value_outside_rule = []

        for index, row in self.get_sheet_as_dataframe().iterrows():
            cell_value = row[self.main_column]

            if cell_value != '':
                if isinstance(cell_value, str):
                    row_value_outside_rule.append([index, cell_value])
                elif cell_value < min_number or cell_value > max_number:
                    row_value_outside_rule.append([index, cell_value])

        return [row_value_outside_rule, "Checa se os valores estão entre um intervalo específico e ignora células sem preenchimento."]

    def specify_checking(self) -> list:
        match self.checking_type:
            case '03':
                return self.check_value_range_and_ignore_blank_cell()
            case _:
                return ["", ""]

    def do_checking_and_send_email(self) -> dict:
        checking_result = self.specify_checking
        if checking_result[0] > 0:
            self.send_email()
