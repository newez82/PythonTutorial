"""
 scrape information from the website

    1 - install beautifulsoup library
         pip install beautifulsoup4

    2 - install lxml parser or html5 parser
         pip install lxml
         pip install html5lib

    3 - install request library
         pip install request
"""

import csv

import requests
from bs4 import BeautifulSoup

# pass html in a string or pass it as a file
with open(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\22.web_scraping\\simple.html",
    encoding="UTF-8",
) as html_file:
    soup = BeautifulSoup(html_file, "lxml")

# print html with indented format
print(soup.prettify())

# print out the first title and text using soup.title
# print out the first title text only using soup.title.text
match = soup.title.text
print("get the text from the title tag:", match)

# use find() method to do something similar above but also find
# the exact tag that we are looking for
# we can pass argument of id if div has id argument
# we pass class_ because class is a special keyword in python
match = soup.find("div", class_="footer")
print("get the div with the class of footer:", match)

# get the headline and snip it from article on the page using find() method
article = soup.find("div", class_="article")
headline = article.h2.a.text
print("get the headline from the article:", headline)

summary = article.p.text
print("get the summary from the article:", summary)

# get the headline and snip it from each article on the page using find_all() method
for article in soup.find_all("div", class_="article"):
    headline = article.h2.a.text
    print("get the headline from the article using find_all() method:", headline)

    summary = article.p.text
    print("get the summary from the article using find_all() method:", summary)

    print()


############################################################################
#                   scape from actual websiute
############################################################################
# get source code from the webiste using request library
# get() method will return a response object and
# using .text to get the source code
source = requests.get(
    "https://invidious.nerdvpn.de/channel/UCCezIgC97PvUuR4_gbFUs5g"
).text
soup = BeautifulSoup(source, "lxml")
body = soup.find("body")
# print(body.prettify())
video_title = body.find("div", class_="video-card-row").a.p.text
print("title:", video_title)

video_src = body.find("div", class_="thumbnail").a["href"]
print("video_src:", video_src)

video_id = video_src.split("/")[1]
video_id = video_src.split("?")[1]
video_id = video_src.split("=")[1]
print("video_id:", video_id)

link = f"https://invidious.nerdvpn.de/watch?v={video_id}"
print("link:", link)


csv_file = open("C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\22.web_scraping\\cms_scape.csv", "w", encoding="UTF-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["link", "video id"])

# get all videos
for div_indx in soup.find_all("div", class_="thumbnail"):
    div_video_src = div_indx.a["href"]
    #print("div_video_src:", div_video_src)
    try:
        video_id = div_video_src.split("/")[1]
        video_id = div_video_src.split("?")[1]
        video_id = div_video_src.split("=")[1]
        print()

        LINK = f"https://invidious.nerdvpn.de/watch?v={video_id}"

    except Exception as e:
        LINK = None

    print("video_id:", video_id, "link:", LINK)
    csv_writer.writerow([video_id, LINK])

csv_file.close()
