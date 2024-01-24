"""
    1. Duck Typing and Easier to ask forgivness than permission (EAFP).
    2. Duck Typing doesn't care if it's a certain type of object, it only
    care if it can do what we ask.
    3. It slightly faster and it doesn't expect a lof of exceptions beacuse
    it only access the object 1x instead of mulitple access to check the object
    existence.
    4. it is more readable.
"""


class Duck:
    """Duck class"""

    def quack(self):
        """Duck sound"""
        print("Quack, quack")

    def fly(self):
        """Duck behavior"""
        print("Flap, flap")


class Person:
    """Duck class"""

    def quack(self):
        """Duck sound"""
        print("I'm quacking like a duck!")

    def fly(self):
        """Duck behavior"""
        print("I'm flapping my arms!")


def quack_and_fly(thing):
    # Not Duck-Typed(Non Pythonic)
    # LBYL - Look before you leap
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print("This has to be a Duck!")
    # print()

    """
    Pythonic EAFP
    """
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as ae:
        print(ae)


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)


####################################################
#           Example 2 - dictionary
####################################################

person_dict = {"name": "Jess", "age": 23}

# LBYL (Non-Pythonic)
if "name" in person_dict and "age" in person_dict and "job" in person_dict:
    print(
        f"I'm {person_dict['name']}. I'm {person_dict['age']} years old and I am a {person_dict['job']}"
    )
else:
    print("Missing some keys from LBYL Non-Pythonic")

# EAFP (Pythonic)
try:
    print(
        f"I'm {person_dict['name']}. I'm {person_dict['age']} years old and I am a {person_dict['job']}"
    )
except KeyError as ke:
    print(f"Missing {ke} keys from EAFP Pythonic")

####################################################
#           Example 3 - list
####################################################
my_list = [1, 2, 3, 4, 5]

# Non-Pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print("Index does not exists from LBYL Non-Pythonic")


# Pythonic
try:
    print(my_list[5])
except IndexError:
    print("Index does not exists EAFP Pythonic")

####################################################
#           Example 4 - access file
####################################################
import os

MY_FILE = "/temp/test.txt"

# Race condition
if os.access(MY_FILE, os.R_OK):
    with open(MY_FILE, encoding="UTF-8") as f:
        print(f.read())
else:
    print("File can not be accessed")


# No Race condition
try:
    f = open(MY_FILE, encoding="UTF-8")
except IOError as ioe:
    print("File can not be accessed")
else:
    with f:
        print(f.read())
