import pytest
from Week6_Eje5 import count_upper_or_lower_case

def test_count_mixed_case():
    """Test counting upper and lower case letters in a mixed case string"""
    upper, lower = count_upper_or_lower_case("I love Costa Rica")
    assert upper == 3
    assert lower == 11

def test_count_all_uppercase():
    """Test counting a string with all uppercase letters"""
    upper, lower = count_upper_or_lower_case("HELLO")
    assert upper == 5
    assert lower == 0

def test_count_all_lowercase():
    """Test counting a string with all lowercase letters"""
    upper, lower = count_upper_or_lower_case("hello")
    assert upper == 0
    assert lower == 5
