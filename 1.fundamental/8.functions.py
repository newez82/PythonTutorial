"""Functions - allow to reuse code without repeating ourselves    
"""


# Put pass keyword inside the function to fill in function later.
# We don't want to do anything with this for now but it won't
# throw any erros for leaving it blank
def hello_func():
    # pass
    # docstrings help document what a function or a class is supposed to do
    """Function without argument."""
    return "Hi Function."


# customized the function by passing greeting argument,
# the scope of the variable is local to the function.
# pass default value when no value pass into the argument
def hello_greeting_func(greeting, name="You"):
    """Function with argument."""
    return f"{greeting}, {name} Greeting Function."


# Since the function return String, we can use String functions
# to call another method
print(hello_func().upper())

# pass the greeting argument directly when calling the function
print(hello_greeting_func("Hi"))


# *args and **kwargs are allowing us to accept an arbitary number
# of positional or keyword arguments
def student_info(*args, **kwargs):
    """We use *args and **kwargs when we don't know how many
    elements are going to be
        args is tuple with all of our positional arguments
        kwargs is a dictionary of our keyword values
    It unpacks the parameter values and pass them in individually
    """
    print("*args values:", args)
    print("**kwargs values:", kwargs)


student_info("Math", "Art", name="John", age=22)


courses = ["Math", "Art"]
info = {"name": "John", "age": 22}
print(
    "It will pass the list and dictionary objects as it without unpack the value from the object"
)
student_info(courses, info)

print(
    "adding * and ** in front of the list and dictionary will unpack the value from the object"
)
student_info(*courses, **info)


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, Fale for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year"""
    if not 1 <= month <= 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(
    "is 2017 a leap year:",
    is_leap(2017),
    ". How many days in feb in 2017:",
    days_in_month(2017, 2),
)
print(
    "is 2020 a leap year:",
    is_leap(2020),
    ". How many days in feb in 2020:",
    days_in_month(2020, 2),
)
