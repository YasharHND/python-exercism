def primes(limit):
    numbers = [n for n in range(2, limit + 1)]
    for n in range(2, limit + 1):
        i = 2
        while n * i <= max(numbers):
            product = n * i
            if product in numbers:
                numbers.remove(product)
            i += 1
    return numbers
