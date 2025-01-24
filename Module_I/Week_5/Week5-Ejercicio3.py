my_list = [4, 3, 6, 1, 7,8]

print(my_list)

delete_item = my_list.pop(len(my_list) - 1)
my_list.insert(0, delete_item)
delete_item2 = my_list.pop(1)
my_list.append(delete_item2)

print(my_list)