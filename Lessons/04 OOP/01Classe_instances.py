# Python Object Oriented Programming

# Basic of creating and instantiating classes


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@mail.com"
        self.pay = pay


emp_1 = Employee("Hakan", "Pekkaya", 20000)
emp_2 = Employee("Test", "Hakan", 25000)

# print(emp_1)
# print(emp_2)

# emp_1.first = "Hakan"
# emp_1.last = "Pekkaya"
# emp_1.email = "Hakan.Pekkaya@mail.com"
# emp_1.pay = 20000

# emp_2.last = "Test"
# emp_2.first = "Hakan"
# emp_2.email = "Test.Hakan@mail.com"
# emp_2.pay = 25000

print(emp_1.email)
print(emp_2.email)


# Methods
