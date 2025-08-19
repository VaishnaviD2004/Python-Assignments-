# Python program to check if a number is an Armstrong number

# Taking input from user
num = int(input("Enter a number: "))

# Convert number to string for digit count
num_str = str(num)
power = len(num_str)

# Calculate sum of digits raised to the power
armstrong_sum = sum(int(digit) ** power for digit in num_str)

# Check and display result
if num == armstrong_sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
