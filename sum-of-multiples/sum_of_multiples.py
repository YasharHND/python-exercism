def sum_of_multiples(limit, multiples):
    summation = 0
    for n in range(limit):
        if any(n % i == 0 for i in multiples if i > 0):
            summation += n
    return summation
