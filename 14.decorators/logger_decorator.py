"""
    logging
"""
# wrap a decorator into another decorator
from functools import wraps


def my_logger(orig_func):
    """logger function"""
    import logging

    print("logger orig_func name:", orig_func.__name__)
    logging.basicConfig(
        filename=f"C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\14.decorators\\{orig_func.__name__}.log",
        level=logging.INFO,
    )

    @wraps(orig_func)
    def logger_wrapper(*args, **kwargs):
        logging.info(
            "%s function Ran with args: %s, and kwargs: %s",
            orig_func.__name__,
            args,
            kwargs,
        )
        return orig_func(*args, **kwargs)

    return logger_wrapper


def my_timer(orig_func):
    """timer function"""
    import time

    @wraps(orig_func)
    def timer_wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return timer_wrapper


# @my_logger
# def display_with_symbol():
#     """
#     display with @my_logger function
#     """
#     print("display function ran")


# display_with_symbol()


# @my_logger
# def display_info_with_symbol(name, age):
#     """
#     display with @my_logger function
#     """
#     print(f"display_info_with_symbol function ran with arguments({name}, {age})")


# display_info_with_symbol("John", 25)

import time

# apply both decorator in to 1 function by stacking the decorator on top of each other
# it equivalent to display_info_with_symbol_timing = my_logger(my_timer(display_info_with_symbol_timing))


@my_logger
@my_timer
def display_info_with_symbol_timing(name, age):
    """
    display with @my_timer function
    """
    time.sleep(1)
    print(f"display_info_with_symbol function ran with arguments({name}, {age})")


print("wrapper name:", display_info_with_symbol_timing.__name__)
display_info_with_symbol_timing("John", 45)
