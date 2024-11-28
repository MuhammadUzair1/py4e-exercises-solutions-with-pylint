"""
This module calculates the pay based on hours worked and hourly rate.
It includes overtime calculation for hours beyond 40.
"""

hrs = float(input("Enter Hours: "))  # Example input: 45
rate = float(input("Enter the Rate: "))  # Example input: 10.50

# Calculate pay based on hours worked
if hrs <= 40:
    print(hrs * rate)
else:
    print(40 * rate + (hrs - 40) * 1.5 * rate)  # Example answer: 498.75
