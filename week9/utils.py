import pandas as pd
import datetime

def is_working_day(date: datetime.date):
    """
    date를 받아서 근무일인지 확인하는 함수
    연휴는 고려하지 않고, 토/일은 근무일이 아니고 월~금은 근무일
    """
    weekday = date.weekday()
    if weekday in {5, 6}:
        return False
    else:
        return True
# 이 파일을 실행하면 utils.py에 파일이 저장됩니다

def load_data():
    df = pd.read_csv("iris.csv")
    return df


