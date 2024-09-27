import pytest
from Week6_Eje4 import reverse_string

def test_reverse_simple_string():
    """Test reversing a simple string"""
    assert reverse_string("Hola Mundo") == "odnuM aloH"

def test_reverse_empty_string():
    """Test reversing an empty string"""
    assert reverse_string("") == ""

def test_reverse_palindrome_string():
    """Test reversing a palindrome string"""
    assert reverse_string("madam") == "madam"