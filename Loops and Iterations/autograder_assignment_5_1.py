'''
Code for the assignment 5.1 of the course Python for Everybody
'''

LARGEST = None # CONSTANT VALUES VARIABLE SHOULD BE IN UPPERCASE ACCORDING TO PEP8
SMALLEST = None

while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == 'done':
        break
    try:
        num = int(user_input)
        if LARGEST is None or num > LARGEST:
            LARGEST = num
        if SMALLEST is None or num < SMALLEST:
            SMALLEST = num
    except ValueError:
        print("Invalid input")

print("Maximum is", LARGEST)
print("Minimum is", SMALLEST)
