from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    def work(self):
        print("Developer is working")


class Accountant(Employee):
    def work(self):
        print("Accountant is working")


dev_1 = Developer()
acc_1 = Accountant()

print(dev_1)
print(acc_1)