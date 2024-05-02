mi_dictionary = {}
list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

for index in range(0,len(list_a)):
    mi_dictionary[list_a[index]] = list_b[index]

print(mi_dictionary)