from dataclasses import dataclass
import sys
from pandas.core.frame import DataFrame
from pandas import to_datetime, to_numeric
import smartsheet
from smartsheet_dataframe import get_sheet_as_df
from app.config.settings import setting

sys.path.append('..\\config')
token = setting.SMARTSHEET_TOKEN


@dataclass
class Smartsheet:

    sheet_id: str | None
    user_token: str = token

    def get_bearer_authentication(self) -> dict:
        return {'Authorization': f'Bearer {self.user_token}'}

    def get_sheets_name_list(self) -> dict:
        """This returns a list of Sheet objects, where each sheet has an id attribute."""

        sheets_list_url = "https://api.smartsheet.com/2.0/sheets"

        try:
            response = requests.request(
                method="GET", url=sheets_list_url, headers=self.get_bearer_authentication())
        except Exception as e:
            return e
        else:
            return response.json()["data"]

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

    data_table: DataFrame
    checking_type: str
    main_column: str
    auxiliary_column: str = None
    reference_values: str = None

    def check_if_there_is_only_date_in_column(self) -> bool:
        try:
            to_datetime(self.data_table[self.main_column])
        except:
            return False
        else:
            return True

    def check_if_there_is_only_integer_in_column(self) -> bool:
        try:
            to_numeric(self.data_table[self.main_column])
        except:
            return False
        else:
            return True

    def check_value_range_and_ignore_blank_cell(self) -> list:
        min_max_number = self.reference_values.split("|")
        min_number = int(min_max_number[0])
        max_number = int(min_max_number[1])
        row_value_outside_rule = []

        for index, row in self.data_table.iterrows():
            cell_value = row[self.main_column]

            if cell_value != '':
                if isinstance(cell_value, str):
                    row_value_outside_rule.append([index, cell_value])
                elif cell_value < min_number or cell_value > max_number:
                    row_value_outside_rule.append([index, cell_value])

        return [row_value_outside_rule, "Checa se os valores estão entre um intervalo específico e ignora células sem preenchimento."]

    def do_check(self) -> dict:

        match self.checking_type:
            case '01':
                return self.check_if_there_is_only_date_in_column()
            case '02':
                return self.check_if_there_is_only_integer_in_column()
            case '03':
                return self.check_value_range_and_ignore_blank_cell()
