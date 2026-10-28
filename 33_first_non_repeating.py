from collections import Counter

def first_non_repeating(text):
    counts = Counter(text)
    return next((ch for ch in text if counts[ch] == 1), None)
