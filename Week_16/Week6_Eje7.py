# File: C:\Users\jarg0317\OneDrive - Sysco Corporation\Documents\DUAD\Week_16\Week6_Eje3.py

def is_prime(number):
    if number < 2:
        return False
    for digit in range(2, int(number**0.5) + 1):
        if number % digit == 0:
            return False
    return True


def prime_numbers(list_numbers):
    primes = []
    for number in list_numbers:
        if is_prime(number):
            primes.append(number)
    return primes


if __name__ == "__main__":
    # Example usage
    list_numbers = [1, 4, 6, 7, 13, 9, 67]
    print(prime_numbers(list_numbers))
