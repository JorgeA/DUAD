def sum_numbers_list(list_numbers):
    sum_numbers = 0
    for number in list_numbers:
        sum_numbers += number
    return sum_numbers  # Change print to return for testability


if __name__ == "__main__":
    # Example usage
    print(sum_numbers_list([3, 3, 3, 2]))
