"""
    Decorator is a function that take another function as an argument as 
    some kind of functionality and return another function without altering
    the source function that we passed in.
"""


def decorator_func(original_func):
    """
    outer function
    """

    def wrapper_func(*args, **kwargs):
        print(
            f"Wrapper executed the wrapper_func method before {original_func.__name__}() method"
        )
        result = original_func(*args, **kwargs)
        print("Executed After:", original_func.__name__)
        return result

    return wrapper_func


def display():
    """
    display function
    """
    print("display function ran")


decorated_display = decorator_func(display)
print(
    "decorated_display variable is decorator_func.wrapper_func",
    decorated_display.__name__,
)
decorated_display()


# using @decorator_func is same as
# decorated_display_symbol = decorator_func(display_with_symbol)
# decorated_display_symbol()
@decorator_func
def display_with_symbol():
    """
    display with @decorator_func function
    """
    print("display function ran")


display_with_symbol()


@decorator_func
def display_info_with_symbol(name, age):
    """
    display with @decorator_func function
    """
    print(f"display_info_with_symbol function ran with arguments({name}, {age})")


display_info_with_symbol("John", 25)


##############################################################
#           Decorator with Input Argument
##############################################################


# Add input argument as an prefix by adding outer layer
def prefix_decorator(prefix):
    """
    Adding another outer function for input argument
    """

    def decorator_function(original_func):
        """
        outer function
        """

        def wrapper_function(*args, **kwargs):
            print(
                f"{prefix} Wrapper executed the wrapper_func method before {original_func.__name__}() method"
            )
            result = original_func(*args, **kwargs)
            print(prefix, "Executed After:", original_func.__name__)
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator("Testing: ")
def display_info_with_symbol_prefix(name, age):
    """
    display with @decorator_func function
    """
    print(f"display_info_with_symbol function ran with arguments({name}, {age})")


display_info_with_symbol_prefix("Jam", 40)
