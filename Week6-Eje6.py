my_string = 'python-variable-funcion-computadora-monitor'

def order_string(my_string):
    list = (my_string.split("-"))
    new_list = sorted(list, reverse=False)
    new_string = '-'.join(new_list)
    print(new_string)

order_string(my_string)