import math


def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    prime_count = 1
    n = 2
    while True:
        if prime_count == number:
            return n
        n += 1
        if is_prime(n):
            prime_count += 1
