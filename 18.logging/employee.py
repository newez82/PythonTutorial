"""
    logging
"""

import logging

# create a new logger for each file to separate logging on different file
# use __name__ to name the log file to the module name if it get imported.
# it will use __main__ as a name if it run this script directly.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\18.logging\\employee.log"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# the basic root logger configuration can be removed once the above logger is specified
# logging.basicConfig(
#    filename="C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\18.logging\\employee.log",
#    level=logging.INFO,
#    format="%(levelname)s:%(name)s:%(message)s",
# )


class Employee:
    """
    Employee class (Parent)
    """

    num_of_emps = 0
    raise_amount = 1.04

    """
        Constructor - __init__ method will run automatically when calling the Employee Class.
        self is an instance that pass automatically into the method when calling it.
    """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        logger.info("Created Employee: %s - %s", self.fullname, self.email)

    @property
    def fullname(self):
        """
        fullname getter
        """
        return f"{self.first} {self.last}"

    # add @property to access the method like attribute similar to java getter
    @property
    def email(self):
        """
        email getter
        """
        return f"{self.first}.{self.last}@company.com"


EMP_1 = Employee("John", "Smith", 50000)
EMP_2 = Employee("Corey", "Schafer", 80000)
EMP_3 = Employee("Jane", "Doe", 100000)
