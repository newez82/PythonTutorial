"""
    inheritance from Employee Class.
    1. Method resolution order - when we instantiated developers, it first looked at
        the __init__ method in Developer class and it's not going to find it, it will
        walk up ths chain of the inheritance until it finds what it's looking for.
"""
import oop_employee


# inherited Employee class by passing it Employee as an arugment
class Developer(oop_employee.Employee):
    """
    Employee subclass
    """

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # use super().__init__() method to have parent class handle the parent parameters
        # and have developer only handle the prog_lang variable
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "Employee", 60000, "Java")

print("Developer 1 email:", dev_1.email)
print("Developer 1 programming language:", dev_1.prog_lang)

# help() tells us the class definition with Method resolution order
print(help(Developer))
