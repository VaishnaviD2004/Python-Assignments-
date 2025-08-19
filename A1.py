# Python program to calculate sum of digits of a number

# Taking input from user
num = int(input("Enter a number: "))

# Initialize sum
sum_of_digits = 0

# Loop to extract digits
while num > 0:
    digit = num % 10      # get last digit
    sum_of_digits += digit
    num //= 10            # remove last digit

# Display result
print("Sum of digits =", sum_of_digits)
