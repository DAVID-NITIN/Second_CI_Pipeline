import importlib

module = importlib.import_module("34_check_sorted")

def test_34_check_sorted_1():
    assert module.is_sorted([1, 2, 3]) == True

def test_34_check_sorted_2():
    assert module.is_sorted([2, 1]) == False
