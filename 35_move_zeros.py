def move_zeros(values):
    return [x for x in values if x != 0] + [0] * values.count(0)
