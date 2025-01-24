from Ejercicio_Algoritmos_de_ordenamiento import bubble_sort
import pytest


# Test 1: Funciona con una lista pequeña.
def test_bubble_sort_small_list():
    assert bubble_sort([5, 3, 8, 6, 1, 9, 2, 7]) == [1, 2, 3, 5, 6, 7, 8, 9]

# Test 2: Funciona con una lista grande (más de 100 elementos).
def test_bubble_sort_large_list():
    large_list = list(range(100, 0, -1))  # Lista de 100 a 1
    sorted_large_list = list(range(1, 101))  # Lista de 1 a 100
    assert bubble_sort(large_list) == sorted_large_list

# Test 3: Funciona con una lista vacía.
def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

# Test 4: No funciona con parámetros que no sean una lista.
def test_bubble_sort_invalid_input():
    with pytest.raises(TypeError):
        bubble_sort("not a list")