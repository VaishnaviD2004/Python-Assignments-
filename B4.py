# Python program to display all prime numbers till n

# Taking input from user
n = int(input("Enter a number: "))

print(f"Prime numbers up to {n} are:")

for num in range(2, n + 1):   # start from 2 (first prime)
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # check divisibility till sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
