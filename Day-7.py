from collections import Counter
import re

with open("Day-7.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = re.findall(r'\b\w+\b', text)

word_counts = Counter(words)

for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")





























# collections.Counter: A built-in Python class that counts the frequency of elements in a list or iterable (like a dictionary with automatic counting).
# re: The regular expression module used for pattern matching and text cleaning.

# open("sample.txt", "r"): Opens the text file in read mode.
# .read(): Reads the entire content of the file as a single string.
# .lower(): Converts all characters to lowercase to ensure words like The and the are treated the same.

# re.findall(...): Finds all substrings in text that match the given pattern.
# r'\b\w+\b':
# \b: Word boundary
# \w+: Matches one or more alphanumeric characters (letters, digits, underscore)
# This pattern helps extract clean words and ignore punctuation.
#
# Example: For the sentence
# "Python is great!"
# It will return ['python', 'is', 'great']

# This creates a dictionary-like object where keys are words and values are their counts.
# Example output: {'python': 3, 'is': 2, 'fun': 1}


# 💡 In Summary:
# This script:
# Reads a file
# Converts all text to lowercase
# Extracts clean words
# Counts how often each word appears
# Prints the top 10 most common words in the file
