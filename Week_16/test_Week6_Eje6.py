import pytest
from Week6_Eje6 import order_string

def test_order_simple_string():
    """Test ordering a simple hyphen-separated string"""
    result = order_string('python-variable-funcion-computadora-monitor')
    assert result == 'computadora-funcion-monitor-python-variable'

def test_order_single_word():
    """Test ordering a single word (no hyphen separation)"""
    result = order_string('python')
    assert result == 'python'

def test_order_empty_string():
    """Test ordering an empty string"""
    result = order_string('')
    assert result == ''
