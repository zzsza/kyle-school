# test_utils.py를 아래 내용으로 overwrite합니다(-a 옵션 없이!)
import pytest
import pandas as pd
import datetime
from utils import is_working_day, load_data

def test_is_working_day():
    assert is_working_day(datetime.date(2020,7,5)) == False
    assert is_working_day(datetime.date(2020,7,4)) == False
    assert is_working_day(datetime.date(2020,7,6)) == True


@pytest.fixture(scope="session")
def result_fixture():
    result = load_data()
    return result


def test_len(result_fixture):
    assert len(result_fixture) == 150


def test_object_type(result_fixture):
    assert isinstance(result_fixture, pd.DataFrame)



