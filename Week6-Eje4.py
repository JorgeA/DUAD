def reverse_string(my_string):
    for letter in range(len(my_string)-1, -1, -1):
        new_string = (my_string[letter])
        print(new_string)


reverse_string("Hola Mundo")
