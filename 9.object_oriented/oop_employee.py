"""
    Object Oriented Programming
    1. Class is a blueprint to create instances and each unique employee that we create
    using our employee class will be an instance of that class.
    2. Instance variable contain data that is unique to each instance.
    3. Class variables are variables that are shared shared among all instances of a class.
    4. regular method automatically take the instance as the first argument by calling self
    5. class method is same as regular method with addition by adding a decorator to the top called @classmethod.
        Use Class method as alternative constructors to provide multiple ways of creating our objects.
        use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
    6. static method doesn't operate on the instance or the class and doesn't pass any instance variable. 
        it used by calling @staticmethod decorator. This method can’t access or modify the class state.
        Use static methods to create utility functions. 
    7. Inheritance allows us to inherit attributes and methods from a parent class.
    8. dunder method is a built-in method that contains double underscore 
    9. @property decorators - getters, setters and deleters allows us to define a method and we can access
        it like an attribute with
"""
import datetime


class Employee:
    
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
        #self.email = first + '.' + last + '@company.com'

        # Use Employee.num_of_emps instead of self.num_of_emps because with raises, it nice
        # to have that constant class value that can be overriden per instance. In this case,
        # we total number of employees to be different in each instance.
        Employee.num_of_emps += 1

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    # add @property to access the method like attribute similar to java getter
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"
    
    def apply_rasise(self):
        """
            access class variable either access them through the class itself (Employee.raise_amount)
            or an instance of the class (self.rasie_amount).
            We use self.raise_amount to override the raise_amount for different employee.
           """
        self.pay = int(self.pay * self.raise_amount)

    # altering the functionality of a method to where we receive the class as our first argument by calling cls.
    @classmethod
    def set_rasie_amt(cls, amount):
        cls.raise_amount = amount

    # alternative constructor using class method
    # overload default constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # static method similar to java, only for the class
    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5 or day.weekday() == 6):
              return False
        return True
    
    # unambiguous representation of the object, it used for debugging and logging,
    # it used by developer.
    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

    # readable representation of the object, it used as a dispaly to the end-user.
    def __str__(self):
        return f"'{self.fullname}' - '{self.email}'"
    
    # add 2 employees salary
    def __add__(self, other):
        return self.pay + other.pay
    
    # return total len of employee fullname
    def __len__(self):
        return len(self.fullname)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


emp_1.fullname='jim corey'
print('Print out an email of the employee 1:', emp_1.email)
print('Print out an email of the employee 2:', emp_2.email)
print('Print out employee 1 full name:', emp_1.fullname)
print('Print out employee 2 full name:', emp_2.fullname)
del emp_1.fullname

# when calling emp_1.fullname(), it will transform into Employee.fullname(emp_1) by passing
# in the instance to a method in the background.
#print('Print out the employee name using Employee class itself:', Employee.fullname(emp_1))

print('Employee 1 current salary:', emp_1.pay)
emp_1.apply_rasise()
print('Employee 1 salary after 4% raise:', emp_1.pay)

print('Check the variable and method for Employee instance: ', emp_1.__dict__)
print('Check the variable and method for Employee Class: ', Employee.__dict__)

# Change the raise_amount from the Employee class, will change the value for each instance
# Employee.raise_amount = 1.05

# Change the raise_amount from the emp_1 instance, will change the value for emp_1 instance only
# emp_1.raise_amount = 1.05


print('Total number of employees: ', Employee.num_of_emps)

# set all of the class variable and both instances amounts
Employee.set_rasie_amt(1.05)

print("Updated raise amount to 5%:", Employee.raise_amount)
print("Updated raise amount to 5%:", emp_1.raise_amount)
print("Updated raise amount to 5%:", emp_2.raise_amount)


# Create Employee from the string separated by hyphens
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_1 = Employee.from_string(emp_str_1)

print("Creat employee from a string:", new_emp_1.email)


my_date = datetime.date(2024,1,17)
print("Employee work day?", Employee.is_workday(my_date))


print("print out repr dunder: ", repr(emp_1))
print("print out str dunder: ", str(emp_1))

print("print out repr dunder: ", emp_1.__repr__())
print("print out str dunder: ", emp_1.__str__())

print("print out integer add dunder: ", int.__add__(1,2))
print("print out string add dunder: ", str.__add__('a', 'b'))

print("Add 2 employees salary:", emp_1 + emp_2)

print("len('test') is calling 'test'.__len__(): ", 'test'.__len__())

print("total len of employee fullname: ", len(emp_1))