my_string = 'I love Nation Sushi'

def count_upper_or_lower_case(my_string):
    upper_counter = 0
    lower_counter = 0
    for letter in my_string:
        if letter.isupper():
            upper_counter += 1
        elif letter.islower():
            lower_counter += 1
    print(f'Tu String tiene {upper_counter} mayusculas y {lower_counter} minusculas')


count_upper_or_lower_case(my_string)