'''
This code extracts the hour from the 'From ' lines in file and counts the occurrences of each hour.
'''

import sys

# Create an empty dictionary to store the counts
hour_counts = {}

# Prompt for a file name
file_name = input("Enter the file name: ")

try:
    # Open the file
    with open(f'./files/{file_name}', encoding="utf-8") as file_handle:
        # Loop through the lines in the file
        for line in file_handle:
            # Look for lines that start with 'From '
            if line.startswith('From '):
                # Split the line into words
                words = line.split()
                # Extract the time portion from the fifth word
                time = words[5]
                # Split the time portion into hour, minute, and second
                hour = time.split(':')[0]
                # Increment the count for the hour
                hour_counts[hour] = hour_counts.get(hour, 0) + 1

except FileNotFoundError:
    print("File cannot be opened:", file_name)
    sys.exit(1)

# Sort the dictionary by hour and print the counts
for hour, count in sorted(hour_counts.items()):
    print(hour, count)
