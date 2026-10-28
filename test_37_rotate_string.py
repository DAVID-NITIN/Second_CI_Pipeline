import importlib

module = importlib.import_module("37_rotate_string")

def test_37_rotate_string_1():
    assert module.rotate_string('abcd', 1) == 'dabc'

def test_37_rotate_string_2():
    assert module.rotate_string('abcd', 0) == 'abcd'
