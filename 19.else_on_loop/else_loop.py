"""
    else after loop
"""

MY_LIST = [1, 2, 3, 4, 5]
for i in MY_LIST:
    print(i)
# else actual refer to no break, if no break was hit, then execute this code
else:
    print("Hit the For/Else Statement!")


def find_index(to_search, target):
    """
    find index from the list
    """
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return i


name_list = ["Corey", "Rick", "John"]
index_location = find_index(name_list, "Rick6")

print(f"Location of target is index: {index_location}")
