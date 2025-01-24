list_to_order = [5, 3, 8, 6, 1, 9, 2, 7] # O(1)

def bubble_sort_descending(list_to_order):
    for index_outside in range(len(list_to_order)):# O(n)
        for index_inside in range(len(list_to_order) - 1):# O(log n)
            if list_to_order[index_inside] < list_to_order[index_inside + 1]: # O(1)
                list_to_order[index_inside], list_to_order[index_inside + 1] = list_to_order[index_inside + 1], list_to_order[index_inside] # O(1)
    return list_to_order # O(1)

print(bubble_sort_descending(list_to_order)) # O(1)
