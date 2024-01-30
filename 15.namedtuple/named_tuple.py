"""
    Named tuple is a lightweight object that works like a normal tuple but it more readable.
"""

from collections import namedtuple

# red, green, blue but it doesn't what those number are without any comment and
# by just reading off from the code.
color_tuple = (55, 155, 255)
print("Print red value from normal tuple: ", color_tuple[0])

# we can use dictionary but it required more typing to specific each color tag
color_dict = {"red": 55, "green": 155, "blue": 255}
print("Print red value from normal dictionary: ", color_tuple[0])

# we use named tuple is middle ground between a tuple and a dictionary,
# it gives us readability and functionality of tuple.
Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(55, 155, 255)
print("Print red value from named tuple: ", color.red)
white = Color(255, 255, 255)
print("Print blue color of white from named tuple: ", white.blue)
