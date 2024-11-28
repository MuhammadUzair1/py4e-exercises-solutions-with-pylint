"""
This script fetches an HTML page, parses it to find all 'span' tags, 
extracts numeric values within these tags, and calculates their sum.
"""

from urllib import request
from bs4 import BeautifulSoup

# Fetch and parse the HTML page
URL = 'http://py4e-data.dr-chuck.net/comments_2131891.html'
with request.urlopen(URL) as response:
    html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# Find all 'span' tags and calculate the sum of their numeric content
tags = soup('span')
TOTAL_SUM = 0

for tag in tags:
    TOTAL_SUM += int(tag.contents[0])  # Convert the content to an integer and add to the sum

# Print the total sum
print(TOTAL_SUM)
