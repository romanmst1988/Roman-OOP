import pytest

from proba import Employee


@pytest.fixture()
def employee_john():
    return Employee("John", "Smith", 50000)

def test_init(employee_john):
    assert employee_john.name == "John"
    assert employee_john.surname == "Smith"
    assert employee_john.pay == 50000
    assert employee_john.email == "John.Smith@company.com"

def test_is_work(employee_john):
    assert not employee_john.is_work
    employee_john.work()
    assert employee_john.is_work

def test_is_work_not_vacation(employee_john):
    employee_john.go_to_vacation()
    employee_john.work()
    assert not employee_john.is_vacation

def test_is_vacation(employee_john):
    assert not employee_john.is_vacation
    employee_john.go_to_vacation()
    assert employee_john.is_vacation

def test_is_vacation_not_work(employee_john):
    employee_john.work()
    employee_john.go_to_vacation()
    assert not employee_john.is_work

