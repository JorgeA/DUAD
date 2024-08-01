list_to_order = [5, 3, 8, 6, 1, 9, 2, 7]

def bubble_sort(list_to_order):
    for index_outside in range(len(list_to_order)):
        for index_inside in range(len(list_to_order)-1):
            if list_to_order[index_inside] > list_to_order[index_inside+1]:
                list_to_order[index_inside], list_to_order[index_inside+1] = list_to_order[index_inside+1], list_to_order[index_inside]
    return list_to_order

print(bubble_sort(list_to_order))