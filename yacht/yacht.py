YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        return 50 if (
                dice[0] == dice[1] == dice[2] == dice[3] == dice[4]
        ) else 0
    elif category == ONES:
        return sum([d for d in dice if d == 1])
    elif category == TWOS:
        return sum([d for d in dice if d == 2])
    elif category == THREES:
        return sum([d for d in dice if d == 3])
    elif category == FOURS:
        return sum([d for d in dice if d == 4])
    elif category == FIVES:
        return sum([d for d in dice if d == 5])
    elif category == SIXES:
        return sum([d for d in dice if d == 6])
    elif category == FULL_HOUSE:
        dice.sort()
        return sum(dice) if (
                (dice[0] == dice[1] and dice[2] == dice[3] == dice[4] and dice[0] != dice[2]) or
                (dice[0] == dice[1] == dice[2] and dice[3] == dice[4] and dice[0] != dice[3])
        ) else 0
    elif category == FOUR_OF_A_KIND:
        dice.sort()
        return (dice[0] * 4 if dice[0] == dice[1] == dice[2] == dice[3]
                else dice[1] * 4 if dice[1] == dice[2] == dice[3] == dice[4]
                else 0)
    elif category == LITTLE_STRAIGHT:
        dice.sort()
        return 30 if dice[0] == 1 and dice[1] == 2 and dice[2] == 3 and dice[3] == 4 and dice[4] == 5 else 0
    elif category == BIG_STRAIGHT:
        dice.sort()
        return 30 if dice[0] == 2 and dice[1] == 3 and dice[2] == 4 and dice[3] == 5 and dice[4] == 6 else 0
    elif category == CHOICE:
        return sum(dice)
