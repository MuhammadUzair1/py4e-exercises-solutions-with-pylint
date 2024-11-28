"""
Extracting Data from JSON

    Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_57128.json (Sum ends with 10)
"""
import urllib.request
import json

address = input('Enter location: ')
print('Retrieving', address)

with urllib.request.urlopen(address) as url:
    raw = json.loads(url.read().decode())

print('Retrieved', len(str(raw)), 'characters')
data = raw.get("comments")

#print(data)

NUM = TOTAL = 0
for i in enumerate(data):
    tmp = data[i]
    value = tmp.get("count")
    NUM = NUM + 1
    TOTAL = TOTAL + int(value)

print("Count:",NUM)
print("Sum:",TOTAL)
