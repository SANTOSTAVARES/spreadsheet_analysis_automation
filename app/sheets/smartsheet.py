from dataclasses import dataclass
import requests
import sys
from pandas.core.frame import DataFrame
from smartsheet_dataframe import get_sheet_as_df
from pandas import to_datetime, to_numeric
from app.config.settings import setting

sys.path.append('..\\config')
token = setting.SMARTSHEET_TOKEN


@dataclass
class Smartsheet:

    sheet_id: str
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
            return response.json()["data"][0]

    def get_sheet_as_dataframe(self) -> DataFrame:

        try:
            df = get_sheet_as_df(token=self.user_token,
                                 sheet_id=self.sheet_id)
        except Exception as e:
            return e
        else:
            return df


@dataclass
class DataTable:

    data_table: DataFrame
    main_column: str
    auxiliary_column: str
    reference_values: str

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
