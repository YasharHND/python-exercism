def value_of_card(card):
    return 10 if card in {'J', 'Q', 'K'} else 1 if card == 'A' else int(card)


def higher_card(card_one, card_two):
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    return card_one if one > two else card_two if two > one else (card_one, card_two)


def value_of_ace(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return 1 if total > 10 or 'A' in (card_one, card_two) else 11


def is_blackjack(card_one, card_two):
    hand = [card_one, card_two]
    return 'A' in hand and 10 in map(value_of_card, hand)


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
