class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.pay + other.pay

        raise TypeError


class Developer(Employee):

    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# class ExampleClass:
#     pass
#
emp_1 = Employee("Corey", "Schafer", 50000)
dev_1 = Developer("Gooli", "Figo", 50000, "Python")
#
# exm_1 = ExampleClass()
#
res = emp_1 + dev_1
print(res)
#
# for emp_obj in (emp_1, dev_1, exm_1):
#     if issubclass(type(emp_obj), Employee):
#         emp_obj.apply_raise()
#     else:
#         print("Skipp object has no raise method")
#
# # if __name__ == "__main__":

print(issubclass(Developer, Employee)) # Наследуется ли Developer класс от Employee

print(isinstance(dev_1, Developer)) # Создан ли объект dev_1 от класса Developer
print(isinstance(dev_1, Employee)) # Создан ли объект dev_1 от класса Employee
print(isinstance(dev_1, object)) # Создан ли объект dev_1 от класса object