"""
    First-Class Functions: A programming language is said to have first-class functions
    if it treats functions as first-class citizens.

    First-Class Citizen: A first-class citizen(object) in a programming language is an
    entity which supports all the operations generally available to other entities.
    These operations typically include being passed as as argument, returned from a 
    function, and assigned to a variable.

    We should be able to treat functions just like any other object or variable.
"""


def square(x):
    """square function"""
    return x * x


def cube(x):
    """cube function"""
    return x * x * x


# assign a function to a variable, this is one of the aspect of
# what it means to be a first-class function. We can treat variable
# f as a function.
f = square

print("Print square function: ", square)
print("Print variable f: ", f)
print("Execute variable f as square function:", f(5))


# pass functions as arguments and return functions as the result of
# other functions. it's higer-order function
def my_map(func, arg_list):
    """map function that pass in another function and list argument"""
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
print(
    "Print out squares by passing square function and list to a my_map function:",
    squares,
)

cubes = my_map(cube, [1, 2, 3, 4, 5])
print("Print out cubes by passing cube function and list to a my_map function:", cubes)


# return a function from another function, this is another one of the aspect of
# what it means to be a first-class function.


def logger(msg):
    """logger function"""

    def log_message():
        print("Log:", msg)

    return log_message


log_hi = logger("Hi!")
log_hi()


def html_tag(tag):
    """html tag function"""

    def wrap_text(msg):
        print(f"<{tag}>{msg}<{tag}>")

    return wrap_text


print_h1 = html_tag("h1")
print_h1("Test Headline!")
print_h1("Another Headline!")
