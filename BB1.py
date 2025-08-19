def first_last_2chars(s):
    # Check length condition
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]


# Example usage
print("Result :", first_last_2chars("General12"))   # Ge12
print("Result :", first_last_2chars("Ka"))         # KaKa
print("Result :", first_last_2chars("K"))          # Empty String
