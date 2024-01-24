"""
    Generatros advantage over list
        1. it is more readable
        2. it is easier to write in list comprehension.
        3. it has better performance since it is not storing all
            values in memory.
    note: refer 4c.list_comprehensions.py for another generator example
"""


# regular function to caculate from a list
def square_nunbers(nums):
    """Calculate sqaure of the number from a list"""
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_nunbers([1, 2, 3, 4, 5])
print("Calculate sqaure of the number from a list:", my_nums)


# generators
def square_nunbers_gen(nums):
    """
    1. Calculate sqaure of the number from a list using generator
        yield keyword is what makes it a generator.
    2. generator do not store the entire result in memory, when priniting
        it out, it print <generator object square_nunbers_gen at 0x0000025A826F8040>
        instead. it yield 1 result at a time. it's waiting for us to ask for the next result
        by put the variable inside next().

    """
    for i in nums:
        yield i * i


my_nums = square_nunbers_gen([1, 2, 3, 4, 5])

# print("Calculate 1st sqaure of the number from a list:", next(my_nums))
# print("Calculate 2nd sqaure of the number from a list:", next(my_nums))
# print("Calculate 3rd sqaure of the number from a list:", next(my_nums))
# print("Calculate 4th sqaure of the number from a list:", next(my_nums))
# print("Calculate 5th sqaure of the number from a list:", next(my_nums))

# Use for loop instead to print out the next yield value
for num in my_nums:
    print("Calculate sqaure of the number from a list:", num)


my_nums_comprehension = (x * x for x in [1, 2, 3, 4, 5])

print("Calculate sqaure of the number from a generator:", my_nums_comprehension)

for num in my_nums_comprehension:
    print(
        "Calculate sqaure of the number from a generator using for loop:",
        num,
    )

# Once convert a list to generator, it will lose the disvantage of performance
print(
    "Print out all value from generator by converting a generator to a list:",
    list(my_nums_comprehension),
)
