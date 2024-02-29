# Python Object Oriented Programming

# Basic of creating and instantiating classes


class Employee:

    num_of_emps = 1
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@mail.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developper(Employee):
    pass


dev_1 = Developper("Hakan", "Pekkaya", 20000)
dev_2 = Developper("Test", "Hakan", 25000)

# print(dev_1.email)
# print(dev_2.email)

print(help(Developper))
