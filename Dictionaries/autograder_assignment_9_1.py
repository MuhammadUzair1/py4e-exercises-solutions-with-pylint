'''
This code reads a file and parses the file line by line. 
It finds lines that start with 'From ' and extracts the email address.
'''

import sys

email_counts = {}

# Prompt for file name
file_name = input("Enter file name: ")
try:
    with open(f'./files/{file_name}', encoding="utf-8") as file_handle:
        # Process the file line by line
        for line in file_handle:
            line = line.strip()
            # Look for lines that start with 'From '
            if line.startswith('From '):
                words = line.split()
                if len(words) > 1:  # Ensure the line has enough words
                    email = words[1]
                    email_counts[email] = email_counts.get(email, 0) + 1

except FileNotFoundError:
    print("File not found:", file_name)
    sys.exit(1)

# Find the most prolific committer
MAX_COUNT = None
MAX_EMAIL = None

for email, count in email_counts.items():
    if MAX_COUNT is None or count > MAX_COUNT:
        MAX_EMAIL = email
        MAX_COUNT = count

# Output the result
if MAX_EMAIL:
    print(MAX_EMAIL, MAX_COUNT)
