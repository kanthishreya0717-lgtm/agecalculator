from calculate_aget import calculate_age
from datetime import date

def test_age_for_past_birthday():
    today = date.today()
    age = calculate_age(2000, 1, 1)
    expected = today.year - 2000
    assert age == expected

def test_age_for_future_birthday_this_year():
    today = date.today()

    if today.month < 12:
        age = calculate_age(2000, 12, 31)
        expected = today.year - 2000 - 1
        assert age == expected

def test_newborn():
    today = date.today()
    age = calculate_age(today.year, today.month, today.day)
    assert age == 0