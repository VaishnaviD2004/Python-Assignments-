def swap_first_two(a, b):
    # If either string length is less than 2, just return as is
    if len(a) < 2 or len(b) < 2:
        return a + " " + b

    # Swap first two characters
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    # Join with a space
    return new_a + " " + new_b


# Example usage
s1 = "abc"
s2 = "xyz"

print("Result:", swap_first_two(s1, s2))
