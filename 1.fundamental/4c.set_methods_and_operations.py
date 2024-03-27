"""
    set methods and operations
"""

# create a set with a list of values set
# ([1, 2, 3, 4, 5]) or {1, 2, 3, 4, 5}
# create empty set - set()
set1 = set([1, 2, 3, 4, 5])
set2 = {7, 8, 9}
# add a new value in a set
set1.add(6)
# add a list values and set2 in set1
set1.update([7, 8, 9], set2)
# remove value from a set
set1.remove(5)
# discard a value instead of remove to prevent in key error since it doesnt exists
set1.discard(99)
print("give us the value that  exists in set1: ", set1)


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

# give us the values that exsts in s1, s2 and s3
s4 = s1.intersection(s2, s3)
print("give us the values that exsts in s1, s2 and s3:", s4)

# give us the values that exists in s1 but not in s2
s4 = s1.difference(s2)
print("give us the values that exists in s1 but not in s2:", s4)

# give us the values that not exists in both s1 and s2
s4 = s1.symmetric_difference(s2)
print("give us the values that not exists in both s1 and s2:", s4)

# create a new list with unique value
list1 = [1, 2, 3, 1, 2, 3]
# cast the set to a list
list2 = list(set(list1))
print("create a new list with unique value:", list2)


employees = ["Corey", "Jim", "Steven", "April", "Judy", "Jenn", "John", "Jane"]
gym_members = ["April", "John", "Corey"]
developers = ["Judy", "Corey", "Steven", "Jane", "April"]

# give us a employees who are gym members and developers
result = set(gym_members).intersection(developers)
print("give us a employees who are gym members and developers:", result)

# give us a employees who are neither gym members and developers
result = set(employees).difference(gym_members, developers)
print("give us a employees who are neither gym members and developers:", result)
