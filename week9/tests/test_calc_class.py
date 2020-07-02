import pytest
from calc_class import Calculator

# 상수
NUMBER_1 = 3.0
NUMBER_2 = 2.0

# Fixtures
@pytest.fixture
def calculator():
    return Calculator()

def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer


# ======Test Cases 시작======
def test_last_answer_init(calculator):
    # TODO : Test Code


def test_add(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test


def test_subtract(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test


def test_subtract_negative(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test


def test_multiply(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test


def test_divide(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test


def test_divide_by_zero(calculator):
    # TODO : ZeroDivisionError가 나오는지 확인하는 Test


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_1),
    (NUMBER_2, NUMBER_1, NUMBER_1),
    (NUMBER_1, NUMBER_1, NUMBER_1),
])
def test_maximum(calculator, a, b, expected):
    # TODO : parametrize를 사용해 파라미터를 주입


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_2, NUMBER_2, NUMBER_2),
])
def test_minimum(calculator, a, b, expected):
    # TODO : parametrize를 사용해 파라미터를 주입


 



