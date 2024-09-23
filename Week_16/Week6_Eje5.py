def count_upper_or_lower_case(my_string):
    upper_counter = 0
    lower_counter = 0
    for letter in my_string:
        if letter.isupper():
            upper_counter += 1
        elif letter.islower():
            lower_counter += 1
    return upper_counter, lower_counter  # Return counts for testing


if __name__ == "__main__":
    # Example usage
    my_string = 'I love Costa Rica'
    upper, lower = count_upper_or_lower_case(my_string)
    print(f'Tu String tiene {upper} mayusculas y {lower} minusculas')
