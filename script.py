"""VSC and git tutorial"""
import sys

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


greet_person = greet("Chin")
print(greet_person)
print("")
