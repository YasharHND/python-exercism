suffixes = [
    "",
    " thousand",
    " million",
    " billion"
]

ones = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

teens = [
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

tens = [
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninty"
]


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    if number % 1000 == 0:
        suffix = 0
        while number >= 1000:
            number //= 1000
            suffix += 1
        return say_three_pack(number) + suffixes[suffix]
    out = ""
    i = 0
    while True:
        part = number % 1000
        out = say_three_pack(part, suffixes[i]) + " " + out
        i += 1
        number = (number - part) // 1000
        if number == 0:
            break
    return out.strip()


def say_three_pack(number, suffix=""):
    if number < 10:
        return ones[number] + suffix
    if number < 100:
        ten = tens[(number // 10) - 1]
        if number % 10 == 0:
            return ten + suffix
        if number < 20:
            return teens[number - 11]
        return ten + "-" + ones[(number % 10)] + suffix
    return ones[number // 100] + " hundred " + say_three_pack(number % 100) + suffix
