# Python program to check if a number is a Perfect Number

# Taking input from user
num = int(input("Enter a number: "))

# Initialize sum of divisors
sum_of_divisors = 0

# Find divisors (excluding the number itself)
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

# Check if perfect number
if sum_of_divisors == num and num != 0:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
