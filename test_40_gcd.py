import importlib

module = importlib.import_module("40_gcd")

def test_40_gcd_1():
    assert module.gcd(12, 18) == 6

def test_40_gcd_2():
    assert module.gcd(0, 5) == 5
