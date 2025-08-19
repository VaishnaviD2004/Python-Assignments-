def remove_odd_index_chars(s):
    # Keep only characters at even indices
    return s[::2]

# Example usage
string = input("Enter a string: ")
result = remove_odd_index_chars(string)
print("String after removing odd index characters:", result)
