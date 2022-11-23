import re


class PhoneNumber:
    def __init__(self, number):
        number = re.sub(r"[ +()\-\.]+", "", number)
        if len(number) < 10:
            raise ValueError("incorrect number of digits")
        if len(number) > 11:
            raise ValueError("more than 11 digits")
        if len(number) == 11:
            if number[0] == "1":
                number = number[1:]
            else:
                raise ValueError("11 digits must start with 1")
        if number[0] == "0":
            raise ValueError("area code cannot start with zero")
        if number[0] == "1":
            raise ValueError("area code cannot start with one")
        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")
        if re.search(r"[@:!]+", number):
            raise ValueError("punctuations not permitted")
        if re.search(r"[a-zA-Z]+", number):
            raise ValueError("letters not permitted")
        self.number = number
        self.area_code = number[:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
