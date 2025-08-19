def count_repeated_chars(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    # Print only characters with frequency > 1
    for ch, count in counts.items():
        if count > 1:
            print(ch, count)


# Example usage
string = "thequickbrownfoxjumpsoverthelazydog"
count_repeated_chars(string)

