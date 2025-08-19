# Python program to display list elements in reverse order

# Create a list
my_list = []

# Accept number of elements
n = int(input("Enter number of elements: "))

# Input elements from user
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

# Display original list
print("\nOriginal List:", my_list)

# Display list in reverse order (method 1)
print("Reversed List (using slicing):", my_list[::-1])

# Display list in reverse order (method 2 - loop)
print("Reversed List (using loop):")
for i in range(len(my_list)-1, -1, -1):
    print(my_list[i], end="  ")
