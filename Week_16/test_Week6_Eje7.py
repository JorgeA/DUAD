import pytest
from Week6_Eje7 import prime_numbers

def test_prime_numbers_mixed_list():
    """Test prime numbers in a list with mixed prime and non-prime numbers"""
    result = prime_numbers([1, 4, 6, 7, 13, 9, 67])
    assert result == [7, 13, 67]

def test_prime_numbers_empty_list():
    """Test prime numbers when given an empty list"""
    result = prime_numbers([])
    assert result == []

def test_prime_numbers_no_primes():
    """Test prime numbers when no prime numbers are present"""
    result = prime_numbers([4, 6, 8, 9, 10])
    assert result == []
