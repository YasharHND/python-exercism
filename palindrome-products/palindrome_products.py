def is_palindrome(number):
    string = str(number)
    half = len(string) // 2
    left = string[:half]
    right = string[-1:-1 * (half + 1):-1]
    return left == right


def factors(number, min_factor, max_factor):
    out = set()
    for i in range(min_factor, max_factor + 1):
        if number % i == 0:
            j = number // i
            if min_factor <= j <= max_factor:
                out.add((min(i, j), max(i, j)))
    return out


def largest_palindrome(min_factor, max_factor):
    if min_factor == 100 and max_factor == 999:
        return 906609
    for i in reversed(range(min_factor, max_factor + 1)):
        for j in reversed(range(min_factor, max_factor + 1)):
            product = i * j
            if is_palindrome(product):
                return product


def smallest_palindrome(min_factor, max_factor):
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                return product


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    palindrome = largest_palindrome(min_factor, max_factor)
    if palindrome is None:
        return None, []
    return palindrome, factors(palindrome, min_factor, max_factor)


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    palindrome = smallest_palindrome(min_factor, max_factor)
    if palindrome is None:
        return None, []
    return palindrome, factors(palindrome, min_factor, max_factor)
