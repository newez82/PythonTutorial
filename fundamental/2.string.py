"""Print Welcome Message"""
FIRST_MESSAGE = "Hello World"
print("first message:", FIRST_MESSAGE)

# multi-line string by using 3 quotes at the beinning and end of the string
MULTI_LINE_MESSAGE = """Hello's World was a good
cartoon in the 1990s"""
print("multi-line message:", MULTI_LINE_MESSAGE)

# find how many characters in the string
print("length of first message using str(len(FIRST_MESSAGE)):", str(len(FIRST_MESSAGE)))

# find the first character of the string
print("first character of first message using FIRST_MESSAGE[0]:", FIRST_MESSAGE[0])

# find the last character of the string
print("last character of first message using FIRST_MESSAGE[10]:", FIRST_MESSAGE[10])

# find only hello from the first message
print(
    "find only hello from the first message using FIRST_MESSAGE[0:5]:",
    FIRST_MESSAGE[0:5],
)

# python will assume to start from the beginning if we leave off the 0 in slicing
print(
    "find only hello from the first message using FIRST_MESSAGE[:5]:"
    + " by not providing starting index:",
    FIRST_MESSAGE[:5],
)

# find the World from the first message using FIRST_MESSAGE[6:] by leaving off the end index
print(
    "find only world from the first message using FIRST_MESSAGE[6:]"
    + " by not providing end index:",
    FIRST_MESSAGE[6:],
)

# set lower case for the first message using method lower()
print("print lowercase of first message using .lower(): ", FIRST_MESSAGE.lower())

# set upper case for the first message using method upper()
print("print lowercase of first message using .upper(): ", FIRST_MESSAGE.upper())

# count number of word in the message using count() method
print(
    "count number of hellow in first message using FIRST_MESSAGE.count('Hello'):",
    FIRST_MESSAGE.count("Hello"),
)

# count number of character l in the message using count() method
print(
    "count number of hello in first message using FIRST_MESSAGE.count('l'):",
    FIRST_MESSAGE.count("l"),
)

# find the word "World" in FIRST_MESSAGE using find() method
# it will return the the index where the word is starting
# or return -1 if it doesn't exists
print(
    "find the word 'World' in first message using FIRST_MESSAGE.find('World'):",
    FIRST_MESSAGE.find("World"),
)

# replace character in first message with
# another character using replace() method
REPLACE_MESSAGE = FIRST_MESSAGE.replace("World", "Universe")
print("replace the word 'world' with 'universe' in the first message:", REPLACE_MESSAGE)

# Concat strings with the following options:
# 1. greeting + ', ' + name + '. Welcome!'
# 2. format string: {}, {}. Welcome!".format(greeting, name)
# 3. f string: f"{GREETING}, {NAME.upper()}. Welcome!"
GREETING = "Hello"
NAME = "Chin"
GREETING_MESSAGE = f"{GREETING}, {NAME.upper()}. Welcome!"
print("Concat text with f string: ", GREETING_MESSAGE)


# print out the type of an object using type() method
NUM_100 = "100"
print("print out the type of variable NUM_100:", type(NUM_100))

# Cast String to integer
NUM_100 = int("100")
print("Cast String to integer:", NUM_100)
print("print out the type of variable NUM_100 after casting to integer:", type(NUM_100))


# Show all attributes and methods that we have access to with that variable using dir() method
print(
    "Show all attributes and methods that we have access to with NAME variable using dir() method",
    dir(NAME),
)

# give a detail description of what the methods do using help() method
help(str.lower)

help(str.center)

print(FIRST_MESSAGE.center(3))
