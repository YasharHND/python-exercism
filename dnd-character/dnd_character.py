import random


def roll_dice():
    result = [random.randint(1, 6) for _ in range(4)]
    result.remove(min(result))
    return sum(result)


def modifier(value):
    return (value - 10) // 2


class Character:
    def __init__(self):
        self.strength = roll_dice()
        self.dexterity = roll_dice()
        self.constitution = roll_dice()
        self.intelligence = roll_dice()
        self.wisdom = roll_dice()
        self.charisma = roll_dice()
        self.abilities = [
            self.strength,
            self.dexterity,
            self.constitution,
            self.intelligence,
            self.wisdom,
            self.charisma
        ]
        self.hitpoints = modifier(self.constitution) + 10

    def ability(self):
        return self.abilities[random.randint(0, 5)]
