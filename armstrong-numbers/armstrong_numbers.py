def is_armstrong_number(number):
    power = len(str(number))
    sum_ = 0
    messed_up_number = number
    while messed_up_number != 0:
        digit = messed_up_number % 10
        messed_up_number = (messed_up_number - digit) // 10
        sum_ += digit ** power
    return sum_ == number

