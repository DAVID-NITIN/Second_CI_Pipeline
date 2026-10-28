import importlib

module = importlib.import_module("36_most_frequent")

def test_36_most_frequent_1():
    assert module.most_frequent([1, 2, 2, 3]) == 2

def test_36_most_frequent_2():
    assert module.most_frequent([]) == None
