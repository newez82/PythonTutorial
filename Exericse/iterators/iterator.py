"""
    Create a Sentence class for iterator
    Create a generator with the same functionality

    output will be
    This
    is 
    a
    test
"""


class Sentence:

    def __init__(self, str):
        self.str = str
        self.index = 0
        self.words = self.str.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentence = Sentence("This is a test")
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))


def words_generator(sentence):
    """
    iteator on generator
    """
    for word in sentence.split():
        yield word


split_sentence = words_generator("This is a test generator")
print(next(split_sentence))
print(next(split_sentence))
print(next(split_sentence))
print(next(split_sentence))
print(next(split_sentence))
