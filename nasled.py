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

class Developer(Employee):

    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # self.first = first
        # self.last = last
        # self.pay = pay
        self.prog_lang = prog_lang

if __name__ == "__main__":
    dev_1 = Developer("Gooli", "Figo", 50000, "Python")
    print(dev_1.first)
    print(dev_1.last)
    print(dev_1.pay)
    print(dev_1.prog_lang)

#    emp_1 = Employee("Corey", "Schafer", 50000)
#    print(emp_1.pay)
#    emp_1.apply_raise()
#    print(emp_1.pay)
#
#    dev_1 = Developer("Gooli", "Figo", 50000)
#    print(dev_1.pay)
#    dev_1.apply_raise()
#    print(dev_1.pay)




