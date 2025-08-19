# Define string
str1 = "Python"

# Print whole string
print(str1)        # Output: Python

# Print first character
print(str1[0])     # Output: P

# Iterate directly over string
for i in str1:
    print(i, end="  ")   # Output: P  y  t  h  o  n
print()  # new line

# Iterate using index
for i in range(len(str1)):
    print(str1[i], end="  ")   # Output: P  y  t  h  o  n
