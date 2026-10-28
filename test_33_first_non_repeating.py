import importlib

module = importlib.import_module("33_first_non_repeating")

def test_33_first_non_repeating_1():
    assert module.first_non_repeating('swiss') == 'w'

def test_33_first_non_repeating_2():
    assert module.first_non_repeating('aabb') == None
