# Python program to check if input value is in range 1 to 50
import sys

# Check if user provided an argument
if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
else:
    # Convert command line argument to integer
    num = int(sys.argv[1])

    # Check range
    if 1 <= num <= 50:
        print("Ok")
    else:
        print("Out of range")
