from collections import Counter

def most_frequent(values):
    return Counter(values).most_common(1)[0][0] if values else None
