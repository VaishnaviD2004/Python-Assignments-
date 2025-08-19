# Python program to display alternate characters of string from both directions

# Take input string
s = input("Enter a string: ")

# Alternate characters from left to right
print("Alternate characters (Left to Right):", s[::2])

# Alternate characters from right to left
print("Alternate characters (Right to Left):", s[::-2])
