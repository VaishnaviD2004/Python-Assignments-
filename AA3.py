# Python program to count vowels and consonants in a string

# Take input string
s = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Counters
vowel_count = 0
consonant_count = 0

# Loop through characters
for ch in s:
    if ch.isalpha():  # consider only alphabets
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display result
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
