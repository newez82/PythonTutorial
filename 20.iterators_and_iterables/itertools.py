"""
    itertools is a collection of tools that allow us to work with iterators in a fast
    and memory efficient way.
    itertools moduel contains a number of commonly used iterators as well as functions 
    for combining several iterators.
"""

import itertools
import operator

# count() method simply returns an iterator that count, if no arguement passed in, it will
# start at 0 and count bout by 1 each iteration. it will never stop if using for or while
# loop. we can just print the next value using next() method.
counter = itertools.count()

data = [100, 200, 300, 400]
# zip() method combines 2 intervals and pairs the values together.
# it will end in the shortest iterable, which is data list.
# itertools.count() will keep grabbing the next value until our
# data list had gone through all of its values. The count() method
# will work on any size of data
daily_data = list(zip(itertools.count(), data))
print("Pair up the count value with the data list: ", daily_data)

# Start the count value other than 0 by passing in the value of start
# and counting up by 5 by passing in the value of step
counter_start_from = itertools.count(start=5, step=5)
print("Count start from 5 and counting up by 5: ", next(counter_start_from))
print("Count start from 5 and counting up by 5: ", next(counter_start_from))
print("Count start from 5 and counting up by 5: ", next(counter_start_from))
print("Count start from 5 and counting up by 5: ", next(counter_start_from))

# it can count back and by decimal by passing step = -2.5. it will
# substracts 2.5 from each step and even goes into the negatives
counter_backward = itertools.count(start=5, step=-2.5)
print("Count start from 5 and counting up by 5: ", next(counter_backward))
print("Count start from 5 and counting up by 5: ", next(counter_backward))
print("Count start from 5 and counting up by 5: ", next(counter_backward))
print("Count start from 5 and counting up by 5: ", next(counter_backward))

# zip_longest() is similar to zip() method except it doesn't end until the longest
# iterable is exhausted. it will continue with range and it will continue
# to use the None value.
zip_longest_data = list(itertools.zip_longest(range(10), data))
print(
    "Pair up the count value with the data list using zip_longest: ", zip_longest_data
)


##################################################################
# cycle() method returns an iterator that goees on forever,
# it takes an iterable as an argument and will cycle through
# those values over and over.
##################################################################
cycle_counter = itertools.cycle([1, 2, 3])
print("Cycle through the value over again: ", next(cycle_counter))
print("Cycle through the value over again: ", next(cycle_counter))
print("Cycle through the value over again: ", next(cycle_counter))
print("Cycle through the value over again: ", next(cycle_counter))
print("Cycle through the value over again: ", next(cycle_counter))
print("Cycle through the value over again: ", next(cycle_counter))

##################################################################
# repeat() method will takes some input and repeats it
# indefinitely, we can put the limit by passing value of times
# variable. it will through StopIteration exceptino if we print
# more than the times value.
##################################################################
repeat_counter = itertools.repeat(2, times=3)
print("Repeat the same value 3 times: ", next(repeat_counter))
print("Repeat the same value 3 times: ", next(repeat_counter))
print("Repeat the same value 3 times: ", next(repeat_counter))
# print("Repeat the same value 3 times: ", next(repeat_counter))
# print("Repeat the same value 3 times: ", next(repeat_counter))
# print("Repeat the same value 3 times: ", next(repeat_counter))

##################################################################
# map() method
##################################################################
# it will take the first value from the range, and calculate
# zero to the second power, then 1 to the second power, etc.
pow_counter = itertools.repeat(2)
squares = map(pow, range(10), pow_counter)
print("Calculate the power of 2 from the list: ", list(squares))


##################################################################
# star map() method is very similar to map but instead of taking
# arguments from iterables, it instead take arguments that are
# already paired together as tuples.
##################################################################
start_map_squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
print("Calculate the power of 2 from the start map: ", list(start_map_squares))


##################################################################
# functions that terminate the iterator. combinations and
# permutations allow us to take an iterable and return all of the
# cominbations or permutations from that interval.

# combinations are all the different ways that you can group a
# certain number of items or the order does not matter.
# permutations are all the different ways that you can group a
# certain number of items or the order does matter.
##################################################################

letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ["Corey", "Nicole"]

# get all of the possible combinations of 2 values from letters list
# i.e. a, b is equal to b,a so it only show 1 times
combinations_result = itertools.combinations(letters, 2)
for combinations_item in combinations_result:
    print("combinations of 2 values from letters list", combinations_item)

# get all of the possible permutations of 2 values from letters list
permutations_result = itertools.permutations(letters, 2)
for permutations_item in permutations_result:
    print("permutations_item of 2 values from letters list", permutations_item)

# create 4 digits code that can repeat the value by using product function
product_result = itertools.product(numbers, repeat=4)
for product_item in product_result:
    print("4 digits code that can repeat the value", product_item)

# combination with repeated value b using combinations_with_replacement function
combinations_repeat_result = itertools.combinations_with_replacement(numbers, 4)
for combinations_repeat_item in combinations_repeat_result:
    print("combinations repeat values from numbers list", combinations_repeat_item)

##################################################################
# chain() method allows us to chain together intervals, it will
# go through all the items in the first interval and after that
# has been exhausted then it will go through all the items in
# the second interval and so on.
##################################################################

# loop all of the values from all of the lists (letters, numbers and names)
# without creating a new list using chain() method
combined_list = itertools.chain(letters, numbers, names)
for chain_item in combined_list:
    print("Chained all the items from list (letters, numbers, names):", chain_item)


#################################################################
# islice() method allows us to get a slice of an iterator
#################################################################
slice_list = itertools.islice(range(10), 5)
for slice_item in slice_list:
    print("Get first 5 items from the iterable:", slice_item)

# Starting point from 1 instea of 0
slice_list = itertools.islice(range(10), 1, 5)
for slice_item in slice_list:
    print("Get first 5 items from the iterable starting from value of 1:", slice_item)

# Getting every other value by passing in step argument.
slice_list = itertools.islice(range(10), 1, 5, 2)
for slice_item in slice_list:
    print(
        "Get first 5 items from the iterable starting from value of 1 for every other value:",
        slice_item,
    )

# Grab the first few lines from the sample.log file.
with open(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\20.iterators_and_iterables\\sample.log",
    "r",
) as f:
    header = itertools.islice(f, 3)

    for line in header:
        # adding end="" to remove new line character from the print
        # function and the line itself from the file.
        print(line, end="")


#################################################################
# compressed() method allows us to select certain elements from an
# iterable, it similar to filter() method.
#################################################################
selector = [True, True, False, True]
compress_result = itertools.compress(letters, selector)
for compress_item in compress_result:
    print("Get a list of elements that is true from selector list:", compress_item)


def lt_2(n):
    if n < 2:
        return True
    return False


filter_result = filter(lt_2, numbers)
for filter_item in filter_result:
    print("Get a list of elements that is less than 2:", filter_item)


# filter_false() method give us a value that is false instead of true
filter_false_result = itertools.filterfalse(lt_2, numbers)
for filter_false_item in filter_false_result:
    print("Get a list of elements that is greater than or equal 2:", filter_false_item)

#################################################################
# dropwhile() method will drop values from an iterable until
# one of the value return true and return the rest of the iterable.
# it won't filter out all values, only drop the first few one that
# met the criteria.
#################################################################
drop_while_result = itertools.dropwhile(lt_2, numbers)
for drop_while_item in drop_while_result:
    print("drop value from the numbers list:", drop_while_item)

#################################################################
# takewhile() method will grab all the value that return true and
# as soon as it hits a value that doesn't return true, it will
# return the values up to that point.
#################################################################
take_while_result = itertools.takewhile(lt_2, numbers)
for take_while_item in take_while_result:
    print(
        "take value from the numbers list until the value that returned false:",
        take_while_item,
    )

#################################################################
# accumulate() method will takes an iterable and returns
# accumulated sums of each item that is sees and it keeps
# using additiona by default but can use other functions
#################################################################
accumulate_result = itertools.accumulate(numbers)
for accumulate_item in accumulate_result:
    print(
        "accumulate reuslt:",
        accumulate_item,
    )

# pass in mulitply function instead of default addition for
# accumulate() method
accumulate_multiply_result = itertools.accumulate(numbers, operator.mul)
for accumulate_multiply_item in accumulate_multiply_result:
    print(
        "accumulate multiply reuslt:",
        accumulate_multiply_item,
    )

#################################################################
# groupby() method will go through an iterable and group
# values based on a certain key and it will return a stream of
# tuples. Tuples consist of the key that the items were grouped
# on and 2nd value of the tuple is an iterator that contains
# all of the items that were grouped by that key.
#################################################################
people = [
    {"name": "John Doe", "city": "Gotham", "state": "NY"},
    {"name": "Jane Doe", "city": "Kings Landing", "state": "NY"},
    {"name": "Corey Schafer", "city": "Boulder", "state": "CO"},
    {"name": "Al Einstein", "city": "Denver", "state": "CO"},
    {"name": "John Henry", "city": "Hinton", "state": "WV"},
    {"name": "Randy Moss", "city": "Rand", "state": "WV"},
    {"name": "Nicole K", "city": "Asheville", "state": "NC"},
    {"name": "Jim Doe", "city": "Charlotte", "state": "NC"},
    {"name": "Jane Taylor", "city": "Faketown", "state": "NC"},
]


# group the people the state the where from
# group by is different than group by in SQL
# it needed to be sorted before hand
def get_state(person):
    return person["state"]


person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    print(key, len(list(group)))
    for person in group:
        print(person)


#################################################################
# T() method replicate iterator easily,
# once copied, we should not use the original iterator.
#################################################################
copy1, copy2 = itertools.tee(person_group)
