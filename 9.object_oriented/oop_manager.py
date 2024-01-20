"""
    inheritance from Employee Class.
"""

import oop_developer
import oop_employee


class Manager(oop_employee.Employee):
    """
    Employee subclass
    """

    def __init__(self, first, last, pay, employees=None):
        # use super().__init__() method to have parent class handle the parent parameters
        # and have developer only handle the prog_lang variable
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname)


dev_1 = oop_developer.Developer("Corey", "Schafer", 50000, "Python")
dev_2 = oop_developer.Developer("Test", "Employee", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
print("Manager 1 email:", mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
print("Manager 1's team member:")
mgr_1.print_emps()


print("is mgr 1 an instance of Manager class: ", isinstance(mgr_1, Manager))
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
print(
    "is mgr 1 an instance of Employee class: ", isinstance(mgr_1, oop_employee.Employee)
)
print(
    "is mgr 1 an instance of Developer class: ",
    isinstance(mgr_1, oop_developer.Developer),
)
