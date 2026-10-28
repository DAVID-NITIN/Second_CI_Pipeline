import importlib

module = importlib.import_module("38_missing_number_xor")

def test_38_missing_number_xor_1():
    assert module.missing_number([0, 1, 3]) == 2

def test_38_missing_number_xor_2():
    assert module.missing_number([1, 2]) == 0
