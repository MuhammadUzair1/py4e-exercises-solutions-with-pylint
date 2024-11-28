'''
Code for assignment 7.1

In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.
'''

import sys

file_name = input("Enter file name: ")

TOTAL = 0
COUNT = 0

try:
    # Open the file
    with open(f'./files/{file_name}', encoding="utf-8") as file_handle:
        # Loop through each line in the file
        for line in file_handle:
            # Look for lines that start with 'X-DSPAM-Confidence:'
            if line.startswith("X-DSPAM-Confidence:"):
                # Find the numeric value after the colon
                colon_pos = line.find(":")
                try:
                    confidence_value = float(line[colon_pos + 1:].strip())
                    # Increment the TOTAL and COUNT
                    TOTAL += confidence_value
                    COUNT += 1
                except ValueError:
                    print("Invalid confidence value encountered.")

except FileNotFoundError:
    print("File cannot be opened:", file_name)
    sys.exit(0)

# Compute the average if there are valid values
if COUNT > 0:
    average = TOTAL / COUNT
    print("Average spam confidence:", average)
else:
    print("No X-DSPAM-Confidence lines found.")
