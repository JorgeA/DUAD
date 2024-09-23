def order_string(my_string):
    word_list = my_string.split("-")  # Split the string into a list
    new_list = sorted(word_list, reverse=False)  # Sort the list alphabetically
    new_string = '-'.join(new_list)  # Join the sorted list back into a string
    return new_string  # Return the sorted string


if __name__ == "__main__":
    # Example usage
    my_string = 'python-variable-funcion-computadora-monitor'
    print(order_string(my_string))