"""
    iterators - is an object with a state, so that it remembers where it is during iteration.
              - it knows how to get the next value.
              - it has a special method __next__() to get the next value from the iterables.
              - it also has __iter__(), iterators also a iterables that return an object itself.

    iterables - it is something that can be looped over
              - i.e. list is iterables
              - it has a special method __iter__()
"""

nums = [1, 2, 3]
i_nums = iter(nums)

print("iterator: ", i_nums)
print("get a list of dunder method from iterator:", dir(i_nums))
print("get next value from the iterator: ", next(i_nums))
print("get next value from the iterator: ", next(i_nums))
print("get next value from the iterator:", next(i_nums))


# check if the list is iterable by using dir(nums)
# it should has __iter__() method
# for loop is doing in the background is calling __iter__() method
# on our object and returning an iterator that we can loop over
print("get a list of dunder method from the list (iterables):", dir(nums))

for num in nums:
    print(num)


class myRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


num_range = myRange(1, 10)
print("get next value from the myRange object: ", next(num_range))


# create a generator to have same functionality as the class
def my_range_generator(start, end):
    """
    iterator generator method
    """
    current = start
    while current < end:
        yield current
        current += 1


num_range_generator = my_range_generator(1, 10)
print("get next value from the num_range_generator generator: ", next(num_range))
