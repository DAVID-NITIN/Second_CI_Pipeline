def missing_number(values):
    result = len(values)
    for i, value in enumerate(values):
        result ^= i ^ value
    return result
