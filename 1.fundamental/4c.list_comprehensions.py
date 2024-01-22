"""
    list comprehension is an easier and mor readable way to create a list
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# n for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print("Create a copy of a list nums: ", my_list)

my_list = [n for n in nums]
print("Create a copy of a list nums using comprehension: ", my_list)

# n*n for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n * n)
print("Create a list with squares of each number: ", my_list)

my_list = [n * n for n in nums]
print("Create a list with squares of each number using comprehension: ", my_list)

my_list = map(lambda n: n * n, nums)
print("Create a list with squares of each number using map and lambda: ", list(my_list))

# n for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print("Create a list with even number: ", my_list)

my_list = [n for n in nums if n % 2 == 0]
print("Create a list with even number using comprehension: ", my_list)

my_list = filter(lambda n: n % 2 == 0, nums)
print("Create a list with even number using filter and lambda: ", list(my_list))


# (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in "abcd":
    for num in range(4):
        my_list.append((letter, num))
print("Create a list with (letter, num) pair: ", my_list)

my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print("Create a list with (letter, num) pair using comprehension: ", my_list)

#######################################################################
#                      Dictionary Comprehensions
#######################################################################
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", " Wolverine", "Deadpool"]
print(list(zip(names, heros)))

# dict{'name': 'hero'} for each name, hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print("dict{'name': 'hero'} for each name, hero in zip(names, heros)", my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(
    "dict{'name': 'hero'} for each name, hero in zip(names, heros) in comprehension",
    my_dict,
)
#######################################################################
#                      Set Comprehensions
#######################################################################
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9, 10]
my_set = set()
for n in nums:
    my_set.add(n)
print("Create a set from nums list: ", my_set)

my_set = {n for n in nums}
print("Create a set from nums list using comprehensions: ", my_set)
#######################################################################
#                      Generator Expression
# Generator is iterator, a kind of iterable that can only iterate over
# once. It does not store all the values in memroy and generate the
# values on the fly.
# yield is a keyword that is used like return, except the function
# will return a generator.
#######################################################################
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# yield 'n*n' for each 'n' in nums
def gen_func(nums):
    """
    generator function
    """
    for n in nums:
        yield n * n


my_gen = gen_func(nums)
for i in my_gen:
    print(i)

print("Generator comprehensions")
my_gen_comp = (n * n for n in nums)
for i in my_gen_comp:
    print(i)
