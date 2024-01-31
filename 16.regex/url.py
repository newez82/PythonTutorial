"""
    url regex
"""
import re

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# grab all urls

# since we have 3 groups, we can only grab the domain name
# by using group index within the loop
# match.group(0) is entire match
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(3))

# replace the url to domain name and top level domain by
# using back references which refernce the group
# pattern.sub means substitute
subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)
