import importlib

module = importlib.import_module("39_transpose_matrix")

def test_39_transpose_matrix_1():
    assert module.transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_39_transpose_matrix_2():
    assert module.transpose([]) == []
