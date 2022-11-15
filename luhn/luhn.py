def calculate_double(value):
    value *= 2
    return value if value < 10 else value - 9


class Luhn:
    def __init__(self, card_num):
        card_num = card_num.replace(" ", "")
        if card_num[0] == "0":
            card_num = card_num[1:]
        if len(card_num) < 2:
            self.is_valid = False
            return
        if not card_num.isdigit():
            self.is_valid = False
            return
        if len(card_num) % 2 != 0:
            card_num = "0" + card_num
        card_num = [calculate_double(int(card_num[d])) if d % 2 == 0 else int(card_num[d]) for d in range(len(card_num))]
        self.is_valid = sum(card_num) % 10 == 0

    def valid(self):
        return self.is_valid
