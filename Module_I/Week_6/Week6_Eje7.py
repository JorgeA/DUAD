list_numbers = [1, 4, 6, 7, 13, 9, 67]

def is_prime(number):
    if number < 2:
        return False
    for digit in range(2, int(number**0.5) + 1):
        if number % digit == 0:
            return False
    return True


def prime_numbers():
    primes = []
    for number in list_numbers:
        if is_prime(number):
            primes.append(number)
    return primes


print(prime_numbers())