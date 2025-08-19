# Python program to check if a number is Palindrome

# Taking input from user
num = input("Enter a number: ")

# Check palindrome by reversing string
if num == num[::-1]:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")
