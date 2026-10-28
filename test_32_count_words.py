import importlib

module = importlib.import_module("32_count_words")

def test_32_count_words_1():
    assert module.count_words('hello world') == 2

def test_32_count_words_2():
    assert module.count_words('') == 0
