"""
    python file that import custom modules
"""
# import import_modules_9

# use alias mm for the modulles
# import import_modules_9 as mm

# import the function itself instead the whole modules
# it only grant access that that particular function only
# from import_modules_9 import TEST, find_index

# random, math datatime, calendar, os modules are from standard library
import calendar
import datetime
import os
import random

# import sys can help us where to find the module
import sys

# use alias for the function by using as
from import_modules_9 import TEST
from import_modules_9 import find_index as fi

# import everything from the whole module by using *
# however it is hard to track down the issue by which
# module it is importing. It is better to specify the
# function that import from
# from import_modules_9 import *


courses = ["History", "Math", "Physics", "CompSci"]
index = fi(courses, "Math")
print(
    "call find_index function from import_modules_9",
    "by passing in courses list and find the index of Math: ",
    index,
)

print("Print out the variable from the import modules:", TEST)

# first value is the directory where we are currently running the script from
# import_modules_9 is also exists in the directory, thats how it found the module
# second value is the Python Path enviornment variable
# third value is standard library directories
# lastly it is the site-packages dirctory for 3rd party packages
print("To find the modules from local by checking multiple locations using sys.path:")
print(
    "Python is looking for module in the list in the following order:",
    sys.path,
)

# if we move the import_modules_9.py to completely different location - c:\\Python\\lib.
# we will get ModuleNotFoundError. We can solve it with the following approach:
#   1. Add the location to sys.path - sys.path.append('c:\\Python\\lib')
#       this is not a good apprach since it is hardcoded
#       and need to change in muliple locations if needed
#   2. Set it in environment variable
#       variable name: PAYTHONPATH
#       variable value: c:\\Python\\lib


RANDOM_COURSE = random.choice(courses)
print(
    "use random.choice from standard libray to pick a value from a list of courses:",
    RANDOM_COURSE,
)


today = datetime.date.today()
print("print out today date from datetime module:", today)

print("is 2017 a leap year using calendar module:", calendar.isleap(2017))

print(
    "print out the current working directory where this script is located:", os.getcwd()
)

print(
    "print out the location of os file on our filesystem by using thunder(__) attribute:",
    os.__file__,
)
