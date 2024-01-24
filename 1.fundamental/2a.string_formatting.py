"""
    String formatting
"""
person = {"name": "Jenn", "age": 23}

# format without specify the placeholder
SENTENCE = "My name is {} and I am {} years old.".format(person["name"], person["age"])
print("Format without specify the placeholder:", SENTENCE)

# format with specify the placeholder
SENTENCE = "My name is {0} and I am {1} years old.".format(
    person["name"], person["age"]
)
print("Format with specify the placeholder:", SENTENCE)

# f String
SENTENCE = f"My name is {person['name']} and I am {person['age']} years old."
print("Format with f string:", SENTENCE)

# f string in calculatino
CALCULATION = f"4 times 11 is equal to {4 * 11}"
print("calcuation:", CALCULATION)

# f string loop
print("f string in for loop with 0 padding")
for n in range(1, 11):
    SENTENCE = f"The value is {n:02}"
    print(SENTENCE)

# repeating the placeholder
TAG = "h1"
TEXT = "This is a headline"
SENTENCE = "<{0}>{1}</{0}>".format(TAG, TEXT)
print("Repeating the placeholder:", SENTENCE)

# access fields from directly within the placeholders
SENTENCE = "My name is {0[name]} and I am {0[age]} years old.".format(person)
print("Access fields from directly within the placeholders:", SENTENCE)

# access value of a list
my_list = ["Jenn", 23]
SENTENCE = "My name is {0[0]} and I am {0[1]} years old.".format(my_list)
print("Access value of a list:", SENTENCE)


# access object attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_1 = Person("Jack", "33")
SENTENCE = "My name is {0.name} and I am {0.age} years old.".format(person_1)
print("Access object attributes:", SENTENCE)

# pass in keyword arguments to format
SENTENCE = "My name is {name} and I am {age} years old.".format(name="Jenn", age="30")
print("Pass in keyword arguments to format:", SENTENCE)

# unpacking dictionary
SENTENCE = "My name is {name} and I am {age} years old.".format(**person)
print("Unpacking dictionary:", SENTENCE)

# print number with leading 0 by adding colon for formatting with number of padding and up to # of digits
for i in range(11):
    SENTENCE = "The value is {:02}".format(i)
    print(SENTENCE)


# format on decimal places
PI = 3.14159265
SENTENCE = "Pi is equal to {:.2f}".format(PI)
print("Format on decimal places:", SENTENCE)

# format on large number with comma separator
SENTENCE = "1 MB is equal to {:,.2f} bytes".format(1000**2)
print("Format on large number with comma separator:", SENTENCE)

# f string
SENTENCE = f"Pi is equal to {PI:.4f}"
print("f string Format on Pi with 4 deciamls:", SENTENCE)

# format on date
import datetime

my_date = datetime.datetime.today()
print("Current Datetime:", my_date)

SENTENCE = "{:%B %d, %Y}".format(my_date)
print("Print the date with %B %d %Y: ", SENTENCE)

# Get the date foramt for %B %d %Y that fell on Tuesday and was the 061 day of the year
# refer to directive from https://docs.python.org/3/library/datetime.html

SENTENCE = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(
    my_date
)
print(
    "Print the date with %B %d %Y  that fell on Tuesday and was the 061 day of the year: ",
    SENTENCE,
)

SENTENCE = f"Jenn has a birthday on {my_date:%B %d, %Y}"
print("f string on date format", SENTENCE)