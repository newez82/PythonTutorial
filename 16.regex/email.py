"""
    email regex

    Sample Regexs
    [a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""
import re

emails = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

# match the first email address
# Matches lower case and upper case characters within the bracket
# use + sign for 1 or more any of the characters within the bracket
# after the @ symbol, Matches lower case and upper case characters
# within the bracket, use + sign agin to match 1 ore more characters
# end with .com
pattern = re.compile(r"[a-zA-Z]+@[a-zA-Z]+\.com")

# match the first and second email addresses
pattern = re.compile(r"[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)")

# match the all email addresses
pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")

matches = pattern.finditer(emails)

for match in matches:
    print(match)
