"""
    Logging
"""
import logging

logging.basicConfig(
    filename="C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\13.Closures\\example.log",
    level=logging.INFO,
)


def logger(func):
    """logger function"""

    def log_func(*args):
        # use % for logging instead of f string for logging optimization
        logging.info("Running %s function with arguments %s", func.__name__, args)
        print(func(*args))

    return log_func


def add(x, y):
    """add function"""
    return x + y


def substract(x, y):
    """substract function"""
    return x - y


add_logger = logger(add)
sub_logger = logger(substract)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)
