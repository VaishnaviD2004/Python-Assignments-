import string

def word_count(sentence):
    # Remove punctuation
    for p in string.punctuation:
        sentence = sentence.replace(p, "")
    
    # Split into words
    words = sentence.split()
    
    counts = {}
    for word in words:
        word = word.lower()  # make it case-insensitive
        counts[word] = counts.get(word, 0) + 1
    
    return counts


# Example usage
sentence = input("Enter a sentence: ")
result = word_count(sentence)

print("Word occurrences:")
for word, count in result.items():
 print(f"{word}: {count}")
