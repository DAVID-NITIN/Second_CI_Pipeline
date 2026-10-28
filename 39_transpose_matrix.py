def transpose(matrix):
    return [list(row) for row in zip(*matrix)] if matrix else []
