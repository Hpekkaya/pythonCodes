# Python Object Oriented Programming

# Basic of creating and instantiating classes


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@mail.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Hakan", "Pekkaya", 20000)
emp_2 = Employee("Test", "Hakan", 25000)

# print("Before raise :", emp_1.pay)
# emp_1.apply_raise()
# print("After raise  :", emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
