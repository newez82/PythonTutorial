"""
    Closures is a record storing a function together with an environment:
    a mapping associating each free variable of the function with the value
    or storage location to which the name was bound when the closure was created.

    A closure unlike a plain function, allow the function to access those captured
    variables through the closure's reference to them, even when the function is 
    invoked outside their scope. 

    A Closure in simple terms is an inner function that remembers and has access to
    variables in the local scope in which it was created, even after the outer function
    has finished executing.
"""


def outer_func(msg):
    """
    outer function
    """
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func("Hi")
hello_func = outer_func("Hello")
print("hi_func variable is equal to outer_func.inner_func:", hi_func.__name__)

# if we execute my_func copule times, it printed out the message of Hi. We are
# done the execution of outer_func() function but the inner function that we
# returned still has access to that message variable.
hi_func()
hi_func()
hi_func()

hello_func()
