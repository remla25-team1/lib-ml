import pytest
from lib_ml.preprocessing import Preprocessor

def test_process_item_basic():
    pre = Preprocessor()
    text = "I am not happy with this product!"
    result = pre.process_item(text)
    assert isinstance(result, str)
    assert len(result) > 0

def test_process_item_removes_nonalpha():
    pre = Preprocessor()
    text = "Hello!!! 123"
    result = pre.process_item(text)
    assert "123" not in result
    assert "!" not in result

def test_process_item_stopwords():
    pre = Preprocessor()
    text = "This is not a test"
    result = pre.process_item(text)
    assert "not" in result
    assert "is" not in result
