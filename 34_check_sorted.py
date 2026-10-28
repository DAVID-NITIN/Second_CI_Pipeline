def is_sorted(values):
    return all(a <= b for a, b in zip(values, values[1:]))
