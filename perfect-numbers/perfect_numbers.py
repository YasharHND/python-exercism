def aliquot_sum(n):
    summer = 0
    for i in range(1, n):
        if n % i == 0:
            summer += i
    return summer


def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    al_sum = aliquot_sum(number)
    return "perfect" if al_sum == number else "abundant" if al_sum > number else "deficient"
