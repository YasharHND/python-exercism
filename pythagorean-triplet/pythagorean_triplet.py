from math import sqrt, ceil, gcd


def triplets_with_sum(number):
    triplets = []
    for n in range(1, ceil(sqrt(number))):
        for m in range(n + 1, ceil(sqrt(number))):
            if gcd(n, m) > 1 or (n % 2 == 1 and m % 2 == 1):
                continue
            k, a, b, c = 0, 0, 0, 0
            while a + b + c < number:
                k += 1
                a, b, c = calc_triplet(n, m, k)
            if a + b + c == number:
                triplets.append(sorted([a, b, c]))
    return triplets


def calc_triplet(n, m, k):
    return k * (m ** 2 - n ** 2), k * 2 * m * n, k * (m ** 2 + n ** 2)
