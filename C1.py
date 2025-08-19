# Python program to generate number pyramid pattern

# Take input from user
n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    # Increasing part
    for j in range(1, i + 1):
        print(j, end=" ")

    # Decreasing part
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    # New line after each row
    print()
