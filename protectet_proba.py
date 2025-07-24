class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, new_fn):
        first, last = new_fn.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

emp = Employee("John", "Smith")

print(emp.fullname)

emp.fullname = "Corey Schafer"
print(emp.fullname)

del emp.fullname
print(emp.fullname)



