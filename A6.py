# Python program to calculate sum of first and last digit of a number

# Taking input from user
num = int(input("Enter a number: "))

# Get last digit
last_digit = num % 10

# Get first digit
first_digit = num
while first_digit >= 10:
    first_digit //= 10

# Calculate sum
sum_digits = first_digit + last_digit

# Display result
print("Sum of first and last digit =", sum_digits)
