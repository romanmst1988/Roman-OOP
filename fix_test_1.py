class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __str__(self):
        return f"{self.first} {self.last} ({self.pay})"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first}', '{self.last}', {self.pay})"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(f"{self.first} {self.last}")


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Petr", "Petrov", 60000)



sum_pay = emp_1 + emp_2
print(sum_pay)

print(len(emp_1))

print(repr(emp_1))