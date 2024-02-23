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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)


emp_1 = Employee("Hakan", "Pekkaya", 20000)
emp_2 = Employee("Test", "Hakan", 25000)


emp_str_1 = "John-Doe-40000"
emp_str_2 = "Mary-Wane-30000"
emp_str_3 = "Elon-Tart-20000"


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
