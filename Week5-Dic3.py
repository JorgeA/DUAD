list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key in employee.keys():
    if key == list_of_keys[0]:
        key_delete = key
    elif key == list_of_keys[1]:
        key_delete2 = key
delete = employee.pop(key_delete)
delete2 = employee.pop(key_delete2)

print(employee)