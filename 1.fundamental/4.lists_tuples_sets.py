"""Lists and Tuples allow to work on sequential data,
Sets are unordered collections of values with no duplicates.
"""
from operator import attrgetter

# Lists
courses = ["History", "Math", "Physics", "CompSci"]

# print out how many values in the array
print("Print out how many values in the arrays:", len(courses))

# Get first value of the value
print("Get first value of the value:", courses[0])

# Get last value of the value either using courses[3] or courses[-1]
print("Get first value of the value:", courses[-1])

# Get a range of value using slicing
print("Get a range of value using slicing:", courses[:2])

# Append a value into a List by using append() method
courses.append("Art")
print("Append a value into a List by using append() method:", courses)

# Insert a value into a specific location in List by using insert() method
courses.insert(0, "Art")
print(
    "Insert a value into a specific location in List by using insert() method:", courses
)

# Add mulitple values into a list using extend() method
# we can also using append or insert, but it will insert or append
# a list within a list instead of each indiviual values from courses_2 to courses list
# i.e.
# courses.append(courses_2) will give us the following output
# ['History', 'Math', 'Physics', 'CompSci', 'Art', ['Art', 'Education']]
courses_2 = ["Art", "Education"]
courses.extend(courses_2)
print("Add mulitple values into a list using extend() method:", courses)

# Remove Math from the list using remove() method
courses.remove("Math")
print("Remove Math in the list using remove() method:", courses)

# Remove the last value from the list using pop() method
# pop will return the value that removed.
popped = courses.pop()
print("pop will return the value that removed:", popped)
print("Remove the last value from the list using pop() method:", courses)

# Reserve the list that is currently listed using reverse() method
courses.reverse()
print("Reserve the list that is currently listed using reverse() method:", courses)

# Sort the list by using sort() method
courses.sort()
print("Sort the list using sort() method:", courses)

# Sort the number list in ascending order by using sort() method
num = [1, 5, 2, 4, 3]
num.sort()
print("Sort the list using sort() method:", num)

# Sort the number list in descending order by using sort() method with reverse parameter
num.sort(reverse=True)
print("Sort the list using sort() method:", num)

# Sort the list without altering the original list by using sorted() method
courses = ["History", "Math", "Physics", "CompSci"]
sorted_courses = sorted(courses)
print(
    "Sort the list without altering the original list by using sorted() method:",
    sorted_courses,
)

# Sort value by ignoring the negative using sorted() method with key=abs
# it runs each element through this absolute value function before it makes
# the comparsion
li_num = [-6, -5, -4, 1, 2, 3]
sorted_li_num = sorted(li_num, key=abs)
print(
    "ort absolute value using sorted() method by passing key=abs parameter",
    sorted_li_num,
)


class Employee:
    """Sort Employee Object"""

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"({self.name},{self.age}, ${self.salary})"


employee1 = Employee("Carl", 37, 70000)
employee2 = Employee("Sarah", 29, 80000)
employee3 = Employee("John", 43, 90000)

employees = [employee1, employee2, employee3]


def e_sort(employee):
    """Custom Sort function"""
    return employee.name


sorted_employees = sorted(employees, key=e_sort)
print("Sorted employee objects using custom e_sort() method:", sorted_employees)

sorted_employees_lambda = sorted(employees, key=lambda e: e.age)
print("Sorted employee objects using lambda function:", sorted_employees_lambda)

# Sorted employee objects using attrgetter library
sorted_employees_attrgetter = sorted(employees, key=attrgetter("salary"))
print("Sorted employee objects using attrgetter library:", sorted_employees_attrgetter)


# Get the min number out of the list by using min() method
print(
    "Get the min number out of the list by using min() method:",
    min(num),
)

# Get the max number out of the list by using max() method
print(
    "Get the min number out of the list by using max() method:",
    max(num),
)

# Get the sum out of the list by using sum() method
print(
    "Get the sum number out of the list by using sum() method:",
    sum(num),
)

# Find the index of the element in the list by using index() method
print(
    "Find the index of the element in the list by using index() method:",
    courses.index("CompSci"),
)

# Check the element is in the list by using 'in' keyword
print(
    "Find the index of the element in the list by using index() method:",
    "Math" in courses,
)

# loop each value in a list by using for loop
print("loop each value in a list by using for loop")
for course in courses:
    print(course)

# Get the index and value from the for loop by using enumerate() method
print("Get the index and value from the for loop by using enumerate() method")
for index, course in enumerate(courses):
    print(index, course)

# Change the index value instead starting of 0, pass in start=1 parameter
print("Get the index and value from the for loop by using enumerate() method")
for index, course in enumerate(courses, start=1):
    print(index, course)

# Turn List into string separated by delimiter by using join() method

COURSE_STR = ", ".join(courses)
print(
    "Turn List into string separated by delimiter by using join() method:", COURSE_STR
)

# Create a new list by splitting the string with delimiter by using split() method
new_list = COURSE_STR.split(",")
print(
    "Create a new list by splitting the string with delimiter by using split() method:",
    new_list,
)

# create empty list either with empty list clause []
# or built-in list() method
empty_tuple = []
empty_tuple = list()


# Tuple is immutable
tuple_1 = ("History", "Math", " Physics", " CompSci")
print("Tuples is immutable:", tuple_1)

# create empty tuples either with empty tuple clause ()
# or built-in tuple() method
empty_tuple = ()
empty_tuple = tuple()

# tuple doesn't have sort() method, it has to use sorted() function
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print("Sort tuple using sorted() method", s_tup)

# Set is unordered and no duplicate
set_1 = {"History", "Math", " Physics", " CompSci"}
print("Set is unordered and no duplicate:", set_1)

# Set is optimize to check value than list and tuple
print("Set is optimize to check value - Math in set_1:", "Math" in set_1)

# Find 2 set in common by using intersection() method
set_2 = {"History", "Math", " Art", " Design"}
print("Find 2 set in common by using intersection() method:", set_1.intersection(set_2))

# Find 2 set in different by using difference() method
set_2 = {"History", "Math", " Art", " Design"}
print("Find 2 set in difference by using difference() method:", set_1.difference(set_2))

# Combine 2 set by using union() method
set_2 = {"History", "Math", " Art", " Design"}
print("Combine 2 set by using union() method:", set_1.union(set_2))

# Create a empty set by using built-in set() method only,
# using empty set clause {} will create empty dictionary instead
empty_set = set()
