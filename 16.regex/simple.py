"""
    regular expression allow us to search for and match specific patterns of text
    raw string is a string prefixed with an R and print out the string (special character) as it

    .     - Any character except new line
    \d    - Digit (0-9)
    \D    - Not a Digit (0-9)
    \w    - Word Character (a-z, A-Z, 0-9, _)
    \W    - Not a Word Character
    \s    - Whitespace (space, tab, newline)
    \S    - Not whitespace (space, tab, newline)
    \b    - Word boundary (whitespace or a non alphanumeric character)
    \B    - Not a word boundary
    ^     - Beginning of a string
    $     - End of a string
    []    - Matches characters in brackets
    [^ ]  - Matches characters NOT in brackets
    |     - Either Or
    ( )   - Group

    Quantifiers:
    *     - 0 or more
    +     - 1 or more
    ?     - 0 or one
    {3}   - Exact Number
    {3,4} - Range of numbers (Minmum, Maximum)

"""
import re

TEXT_TO_SEARCH = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
"""

SENTENCE = "Start a sentence and the nbring it to an end"

print("Print out with string with tab: \tTab")
print(r"Print out with with special character:\tTab")

# compile method will allos us to separate out our pattern
# into a variable and make it easier to result that variable
# to perform multiple searches
pattern = re.compile(r"abc")

# search with special character by adding backslash (\)
pattern = re.compile(r"coreyms\.com")

# search with word boundary (only match the first word before the space and second word after the space)
pattern = re.compile(r"\bHa")

# search with No word boundary (only match the last 2 words)
pattern = re.compile(r"\BHa")

# search beginning of the word
pattern = re.compile(r"^Start")

# search end of the word
pattern = re.compile(r"$end")

# search phone number with - or .
# it only match 1 character from the string in the bracket
# it doesn't need escape character in the bracket
pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")

# search phone number with - or . and only prefix with 800 or 900
pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")

# match any number in a range of 1 - 5
pattern = re.compile(r"[1-5]")

# match lower case and upper case character by adding back to back
pattern = re.compile(r"[a-zA-Z]")

# match anything that is not lower case and upper case character
# if we put ^ in front inside of the bracket, it will negates the set and
# it matches everthign that is not in that character set
pattern = re.compile(r"[^a-zA-Z]")

# match anything end with 'at' and not prefix with 'b'
pattern = re.compile(r"[^b]at")

# use quantifiers to match more than 1 character at once
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")

# match any characters what prefix wit Mr or Mr.by
# putting '?' since . is optional
# putting '\s' # for a space
# any upper case character in the first letter within the bracket
# putting \w for any word character afterward
# putting * for 0 or more any word character
pattern = re.compile(r"Mr\.?\s[A-Z]\w*")

# use group () to match several different patterns with or (|) character
pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")

# finditer - find all matches in a string and return an iterator that yields match objects.
matches = pattern.finditer(TEXT_TO_SEARCH)
# matches = pattern.finditer(SENTENCE)

# the for loop will give us a result of <re.Match object; span=(1, 4), match='abc'>
# span print out the indexes where to find the characters, which can use for slicing.
for match in matches:
    print(match)

# print("Slicing TEXT_TO_SEARCH form index 1 to 4:", TEXT_TO_SEARCH[1:4])

# open a data.txt and find the phone number
with open(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\16.regex\\data.txt",
    "r",
    encoding="UTF-8",
) as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print("phone number from data.txt file:", match)


################################################################
# findall methods  returns matches as a list of strings
# if it's matching group, it only return the groups
################################################################
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
match_all = pattern.findall(TEXT_TO_SEARCH)

for match in match_all:
    print(match)

################################################################
# match() methods will determine if the regular expression
# matches at the beginning of the string, it doesn't return
# iterable like findall() and finditer() methods does.
# it just returns the first match and return null if no match
################################################################
pattern = re.compile(r"Start")
match_all = pattern.match(SENTENCE)
print(match_all)

################################################################
# search() methods will search entire string for that pattern.
# it likes match, it will find the first match if it finds
################################################################
pattern = re.compile(r"sentence")
search = pattern.search(SENTENCE)
print(search)


################################################################
# flag in regex to ignore upper and lower case by using
# IGNORECASE or I
################################################################
pattern = re.compile(r"start", re.I)
search = pattern.search(SENTENCE)
print(search)
