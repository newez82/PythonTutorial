"""Dictionaries works with key value pairs
"""
student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}

# Print out value from student dictionary
print("Print out value from student dictionary:", student)

# Print out a value from a key in student dictionary by passing
# the key in the []
print("Print out a key from student dictionary by using []:", student["name"])

# Return none instead of error if key doesn't exists in the dictionary
# by using get() method

print(
    "Return none instead of error if key doesn't exists in the dictionar by using get() method:",
    student.get("phone"),
)

# Use the default value that key doesn't exists by passing in the
# default value in the second parameter in the get() method
print(
    "Use the default value that key doesn't exists by passing in the ",
    "default value in the second parameter in the get() method:",
    student.get("phone", "Key Not Found"),
)

# Add a new key into the dictionary
student["phone"] = "555-5555"

print(
    "Use the default value that key doesn't exists by passing in the ",
    "default value in the second parameter in the get() method:",
    student.get("phone", "Key Not Found"),
)

# Update value in the dictionary with the following option:
# 1. Update 1 value in the dictionary
#   student['name'] = 'Jane'
# 2. Update multiple values in the dictionary
# student.update({"name": "Jane", "age": 26, "phone": "888-8888"})
student.update({"name": "Jane", "age": 26, "phone": "888-8888"})
print("Update multiple values in the dictionary by using update() method:", student)

# Remove a specific key and value from the dictionary with the following option:
# 1. Delete a specific key and value from the dictionary by using del keyword
del student["age"]
print(
    "Delete a specific key and value from the dictionary by using del keyword:", student
)
# 2. Delete a specific key and value from the dictionary by using pop() method
student["age"] = 26
age = student.pop("age")
print(
    "pop() method returned the removed value from the list:",
    age,
)
print(
    "Delete a specific key and value from the dictionary by using pop() method:",
    student,
)

# Return number of elements in the dictionary by using len() method
print(
    "Return number of elements in the dictionary by using len() method:", len(student)
)


# Get all the keys from dictionary by using keys() method
print("Get all the keys from dictionary by using keys() method:", student.keys())

# Get all the values from dictionary by using values() method
print("Get all the keys from dictionary by using values() method:", student.values())

# Get all keys and values from dictionary by using items() method
print(
    "Get all keys and values from dictionary by using items() method:", student.items()
)

# sorted() function will sort the key in dictionary
s_dict = sorted(student)
print("Sorted() function sort key in the dictionary:", s_dict)

# Loop throught they key and values using for loop
print("Loop throught they key and values using for loop:")
for key, value in student.items():
    print(key, value)

# Loop from 0 to 9
print("For loop from 0 to 9:")
for i in range(10):
    print(i)

# Loop from starting from index 1
print("Loop from starting from index 1:")
for i in range(1, 11):
    print(i)
