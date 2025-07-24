class Employee:
    name: str
    surname: str
    email: str
    pay: int

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = f"{name}.{surname}@company.com"
        self.is_work = False
        self.is_vacation = False

    def work(self):
        self.is_work = True
        self.is_vacation = False
        print("Do some work")

    def go_to_vacation(self):
        self.is_vacation = True
        self.is_work = False
        print("Go to vacation")



# if __name__ == "__main__":
#     emp_1 = Employee("John", "Smith", 50000)
#
#     print(emp_1)
#     print(emp_1.name)
#     print(emp_1.surname)
#     print(emp_1.pay)
#     print(emp_1.email)


