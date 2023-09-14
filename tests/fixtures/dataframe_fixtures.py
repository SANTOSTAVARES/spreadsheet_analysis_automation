from datetime import date
import pandas as pd
import pytest


@pytest.fixture()
def create_dataframe() -> pd.DataFrame:

    data_to_test = {
        'only_date': [date(year=2022, month=12, day=28),
                      date(year=2022, month=12, day=29),
                      date(year=2022, month=12, day=30),
                      date(year=2022, month=12, day=31),
                      date(year=2023, month=1, day=1)],
        'only_integer': [1, 2, 3, 4, 5],
        'only_float': [1.1, 2.2, 3.3, 4.4, 5.5],
        'integer_and_float': [1, 2, 3, 4.4, 5.5],
        'integer_and_string': [1, 2, 3, 'a', 'b'],
        'only_string': ['a', 'b', 'c', 'd', 'e']
    }
    df = pd.DataFrame(data=data_to_test)

    yield df

    del df
