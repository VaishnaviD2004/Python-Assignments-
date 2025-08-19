# Python program to display multiplication tables within a range

# Accepting range input from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Loop through numbers in the range
for num in range(start, end + 1):
    print(f"\nMultiplication Table of {num}:")
    for i in range(1, 11):   # table from 1 to 10
        print(f"{num} x {i} = {num * i}")
