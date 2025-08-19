# Python program to count character frequency in a string

# Take input string
s = input("Enter a string: ")

# Empty dictionary to store frequency
freq = {}

# Count characters
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Display result
print("Character Frequency:", freq)
