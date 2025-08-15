import pytest

from try_except_study import Employee

def test_raises():
    emp_1 = Employee("Corey", "Schafer", 50000)
    with pytest.raises(TypeError) as e_info:
        emp_1 + "50000"

def test_raises_with_dict():
    emp_1 = Employee("Corey", "Schafer", 50000)
    with pytest.raises(TypeError) as e_info:
        emp_1 + {"1": "2"}