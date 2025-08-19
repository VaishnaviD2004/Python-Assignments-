# Python program to count even, odd, and zero digits in a number

# Taking input from user
num = input("Enter a number: ")

# Initialize counters
even_count = 0
odd_count = 0
zero_count = 0

# Loop through each digit
for digit in num:
    if digit.isdigit():  # ensure it's a digit
        d = int(digit)
        if d == 0:
            zero_count += 1
        elif d % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

# Display result
print("Even digits:", even_count)
print("Odd digits:", odd_count)
print("Zero digits:", zero_count)
