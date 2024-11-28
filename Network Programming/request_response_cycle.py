'''
This code visits a web page and extracts the header fields from the response.
'''

import socket

# Creating a socket connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

CMD = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(CMD)

HEADERS = ""

# Read the response from the server
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # Decode the data and append to the headers string
    HEADERS += data.decode()

# Close the socket
mysock.close()

# Print the raw headers to see the content
print("HTTP Headers:\n", HEADERS)

# Extracting required header fields using simple string search
def get_header_field(headers, field):
    '''Finding the start of the field and extracting the values found'''
    field_start = headers.find(field)
    if field_start != -1:
        # Extract the value of the field
        field_end = headers.find("\r\n", field_start)
        return headers[field_start + len(field):field_end].strip()
    return "Not found"

# Extract each of the required fields
last_modified = get_header_field(HEADERS, "Last-Modified:")
etag = get_header_field(HEADERS, "ETag:")
content_length = get_header_field(HEADERS, "Content-Length:")
cache_control = get_header_field(HEADERS, "Cache-Control:")
content_type = get_header_field(HEADERS, "Content-Type:")

# Print the extracted header fields
print("\nLast-Modified:", last_modified)
print("ETag:", etag)
print("Content-Length:", content_length)
print("Cache-Control:", cache_control)
print("Content-Type:", content_type)
