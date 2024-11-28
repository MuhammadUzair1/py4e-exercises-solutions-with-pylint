"""
Extracting Data from XML

    Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_57127.xml (Sum ends with 12)
"""
import urllib.request
import xml.etree.ElementTree as ET

RESULT = 0

url = input('Enter location: ')

print('Retrieving', url)

with urllib.request.urlopen(url) as uh:
    data = uh.read()

print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print("Count:",len(counts))

for count in counts:
    value = count.text
    RESULT = RESULT + int(value)
print("Sum: ",RESULT)
