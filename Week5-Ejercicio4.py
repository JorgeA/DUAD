my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

for index in range(0,len(my_list)):
    number = my_list[index]
    if number % 2 == 0:
        new_list.append(number)
print(new_list)