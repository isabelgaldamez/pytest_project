import pytest


@pytest.fixture()
def setup_list():
    print("\n  fixtures ...")
    city = ['New York', 'London', 'Singapore', 'San Francisco', 'Sao Paulo']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'Singapore', 'Sao Paulo']

def myReverseList(lst):
    lst.reverse()
    return lst

def test_reverseList(setup_list):
    assert setup_list[::-2] == ['Sao Paulo', 'Singapore', 'New York']
    assert setup_list[::-1] == myReverseList(setup_list)