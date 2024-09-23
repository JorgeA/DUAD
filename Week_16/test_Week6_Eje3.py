import pytest
from Week6_Eje3 import sum_numbers_list

def test_sum_positive_numbers():
    """Test sum of a list with positive numbers"""
    assert sum_numbers_list([3, 3, 3, 2]) == 11

def test_sum_empty_list():
    """Test sum of an empty list"""
    assert sum_numbers_list([]) == 0

def test_sum_with_negative_numbers():
    """Test sum of a list with negative and positive numbers"""
    assert sum_numbers_list([5, -2, 8, -3]) == 8
