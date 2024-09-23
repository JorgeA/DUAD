def reverse_string(my_string):
    new_string = ""
    for letter in range(len(my_string)-1, -1, -1):
        new_string += my_string[letter]  # Build the reversed string
    return new_string  # Return the reversed string


if __name__ == "__main__":
    print(reverse_string("Hola Mundo"))