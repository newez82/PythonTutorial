"""
    DEBUG: Detailed information, typically of interest only when diagnosing problems.
    INFO: Confirmation that things are working as expected.
    WARNING: An indication that something unexpected happened, or 
             indicative of some problem in the near future (e.g. 'disk space low'). 
             The software is still working as expected.
    ERROR: Due to a more serious problem, the software has not been able to perform some function.
    CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

    Default logging is from warning, error and critical and ignore debug and info.

    reference: https://docs.python.org/3/library/logging.html#logrecord-attributes

    look up in python documentation on different Handler
"""

import logging

import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")

file_handler = logging.FileHandler(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\18.logging\\sample.log"
)
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# create a stream handler to show the logging information in the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# since employee class already configured the logging information (root logger), the loggin information
# after the import will be ignore.
# logging.basicConfig(
#     filename="C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\18.logging\\sample.log",
#     level=logging.DEBUG,
#     format="%(asctime)s:%(levelname)s:%(message)s",
# )


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by zero")
    else:
        return result


NUM_1 = 20
NUM_2 = 0

ADD_RESULT = add(NUM_1, NUM_2)
logger.debug("Add: %s + %s = %s", NUM_1, NUM_2, ADD_RESULT)

SUB_RESULT = subtract(NUM_1, NUM_2)
logger.debug("Sub: %s - %s = %s", NUM_1, NUM_2, SUB_RESULT)

MUL_RESULT = multiply(NUM_1, NUM_2)
logger.debug("Mul: %s * %s = %s", NUM_1, NUM_2, MUL_RESULT)

DIV_REUSLT = divide(NUM_1, NUM_2)
logger.debug("Div: %s / %s = %s", NUM_1, NUM_2, DIV_REUSLT)
