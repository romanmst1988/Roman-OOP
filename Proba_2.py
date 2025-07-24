import datetime

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls, new_rase_amt):
        cls.raise_amt = new_rase_amt

    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return True
        return False



# для проверки

# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "Employee", 60000)
#
# print(Employee.raise_amt)
#
# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# emp_str_1 = "Corey-Schafer-70000"
# emp_str_2 = "Test-Employee-60000"
# emp_str_3 = "Elena-Nikitina-90000"

# first, last, pay = emp_str_1.split("-")
# new_emp_1 = Employee(first, last, pay)

# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

my_date = datetime.date(2023, 1, 31)
print(Employee.is_workday(my_date))