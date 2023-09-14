from app.services.sheets import DataChecking
from tests.fixtures.dataframe_fixtures import create_dataframe


def test_if_there_is_only_date_in_column(create_dataframe):
    df = create_dataframe
    data_to_check = DataChecking(data_table=df,
                                 checking_type='01',
                                 main_column='only_date')

    # Check if there is only date on 'only_date' column.
    assert data_to_check.do_check() == True

    # Check if the function return False, when there is not date on column.
    data_to_check.main_column = 'only_string'
    assert data_to_check.do_check() == False
