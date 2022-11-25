pictures = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def find_by_value(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]


def card_value(card):
    number = int(card[:-1]) if card[:-1].isdigit() else pictures.get(card[0])
    return {
        "value": number,
        "symbol": card[-1]
    }


def count_same_cards(hand):
    count = {}
    for card in hand:
        value = card.get("value")
        count.update({value: count.get(value) + 1 if value in count else 1})
    return count


def is_straight_flush_or_either(hand):
    def is_flush(inner_hand):
        return all([card.get("symbol") == inner_hand[0].get("symbol") for card in inner_hand[1:]])

    def is_straight(inner_hand):
        def is_straight_deep(very_inner_hand):
            for i in range(1, 5):
                if very_inner_hand[i].get("value") != very_inner_hand[i - 1].get("value") - 1:
                    break
            else:
                return [card.get("value") for card in very_inner_hand]

        is_normal_straight = is_straight_deep(inner_hand)
        if is_normal_straight:
            return is_normal_straight
        if inner_hand[0].get("value") == 14:
            new_hand = inner_hand[1:] + [{"value": 1, "symbol": inner_hand[0].get("symbol")}]
            is_from_ace_straight = is_straight_deep(new_hand)
            if is_from_ace_straight:
                return is_from_ace_straight

    flush = is_flush(hand)
    straight = is_straight(hand)
    score = 9 if flush and straight else 6 if flush else 5 if straight else None
    if score in (9, 6):
        return score, *[card.get("value") for card in hand]
    if score == 5:
        return score, *straight


def is_four_of_a_kind(counts):
    return any([count == 4 for count in counts.values()])


def is_full_house(counts):
    return len(counts) == 2 and counts[0] == 3 and counts[1] == 2


def is_three_of_a_kind(counts):
    return len(counts) == 3 and counts[0] == 3


def is_two_pair(counts):
    return len(counts) == 3 and counts[0] == 2 and counts[1] == 2


def is_one_pair(counts):
    return len(counts) == 4 and counts[0] == 2


def hand_result(hand):
    straight_flush_or_either = is_straight_flush_or_either(hand)
    if straight_flush_or_either:
        return straight_flush_or_either
    counts = count_same_cards(hand)
    if is_four_of_a_kind(counts):
        return 8, find_by_value(counts, 4), find_by_value(counts, 1)
    sorted_counts = sorted(counts.values(), reverse=True)
    if is_full_house(sorted_counts):
        return 7, find_by_value(counts, 3), find_by_value(counts, 2)
    if is_three_of_a_kind(sorted_counts):
        return 4, find_by_value(counts, 3), *sorted([value for value, count in counts.items() if count == 1], reverse=True)
    if is_two_pair(sorted_counts):
        return 3, *sorted([value for value, count in counts.items() if count == 2], reverse=True), find_by_value(counts, 1)
    if is_one_pair(sorted_counts):
        return 2, find_by_value(counts, 2), *sorted([value for value, count in counts.items() if count == 1], reverse=True)
    return 1, *counts.keys()


def max_hand(hands):
    out = []
    while len(hands) > 0 and len(hands[0]) > 0:
        max_score = max(hands, key=lambda x: x[0])[0]
        out.append(max_score)
        hands = [hand[1:] for hand in hands if hand[0] == max_score]
    return tuple(out)


def best_hands(hands):
    hands_result = []
    for original_hand in hands:
        hand = [card_value(card) for card in original_hand.split()]
        hand.sort(key=lambda x: x.get("value"), reverse=True)
        hands_result.append((hand_result(hand), original_hand))
    max_score = max(hands_result, key=lambda x: x[0])[0]
    return [hand for score, hand in hands_result if score == max_score]
