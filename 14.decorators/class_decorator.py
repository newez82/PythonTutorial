"""
    Class decorator
"""


class DecoratorClass(object):
    """
    decorator class
    """

    def __init__(self, original_func):
        self.original_func = original_func

    # __call__ method enables Python programmers to write classes where
    # the instances behave like functions and can be called like a function.
    def __call__(self, *args, **kwargs):
        print(f"Call method executed before {self.original_func.__name__}() method")
        return self.original_func(*args, **kwargs)


@DecoratorClass
def display_with_symbol():
    """
    display with @decorator_func function
    """
    print("display function ran")


display_with_symbol()


@DecoratorClass
def display_info_with_symbol(name, age):
    """
    display with @decorator_func function
    """
    print(f"display_info_with_symbol function ran with arguments({name}, {age})")


display_info_with_symbol("John", 25)
