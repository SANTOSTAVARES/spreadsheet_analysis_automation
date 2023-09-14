from app.services.sheets import DataChecking
from tests.fixtures.dataframe_fixtures import create_dataframe


def test_if_there_is_only_date_in_column(create_dataframe):
    df = create_dataframe
    data_to_check = DataChecking(data_table=df,
                                 checking_type='01',
                                 main_column='only_date')

    # Check if there is only date on 'only_date' column.
    assert data_to_check.do_check() == True

    # Check if the function return False, when there is not date on 'only_string' column.
    data_to_check.main_column = 'only_string'
    assert data_to_check.do_check() == False


def test_check_if_there_is_only_integer_in_column(create_dataframe):
    df = create_dataframe
    data_to_check = DataChecking(data_table=df,
                                 checking_type='02',
                                 main_column='only_integer')

    # Check if there is only date on 'only_integer' column.
    assert data_to_check.do_check() == True

    # Check if the function return False, when there is not integer on 'only_string' column.
    data_to_check.main_column = 'only_string'
    assert data_to_check.do_check() == False
