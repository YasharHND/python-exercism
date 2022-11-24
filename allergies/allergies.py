book = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats"
}


class Allergies:
    def __init__(self, score):
        self.allergy_list = [name for value, name in book.items() if score & value]

    def allergic_to(self, item):
        return item in self.allergy_list

    @property
    def lst(self):
        return self.allergy_list
