'''
This program reads the file and parses the file line by line
and then splits the line into words and then appends the words into a list.
Print out the second word in the line
'''

import sys

COUNT = 0  # COUNT for 'From ' lines

# Open the file and initialize a count variable
file_name = input("Enter file name: ")
try:
    with open(f'./files/{file_name}', encoding="utf-8") as file_handle:
        # Read the file line by line
        for line in file_handle:
            # Strip whitespace and check for lines starting with 'From '
            line = line.strip()
            if line.startswith('From '):
                # Split the line and print the second word (email address)
                words = line.split()
                if len(words) > 1:  # Ensure there is a second word
                    print(words[1])
                    COUNT += 1

except FileNotFoundError:
    print("File not found: ", file_name)
    sys.exit(0)

# Print the final COUNT
print("There were", COUNT, "lines in the file with From as the first word")
