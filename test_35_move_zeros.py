import importlib

module = importlib.import_module("35_move_zeros")

def test_35_move_zeros_1():
    assert module.move_zeros([0, 1, 0, 2]) == [1, 2, 0, 0]

def test_35_move_zeros_2():
    assert module.move_zeros([1, 2]) == [1, 2]
