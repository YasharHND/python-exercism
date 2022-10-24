def get_rounds(number):
    return [number + i for i in range(3)]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    avg = card_average(hand)
    fl_avg = card_average([hand[0], hand[-1]])
    median = hand[len(hand) // 2]
    return avg == fl_avg or avg == median


def average_even_is_average_odd(hand):
    even = [i for i in hand if i % 2 == 0]
    odd = [i for i in hand if i % 2 != 0]
    avg_even = sum(even) / len(even) if len(even) > 0 else 0
    avg_odd = sum(odd) / len(odd) if len(odd) > 0 else 0
    return avg_even == 0 or avg_odd == 0 or avg_even == avg_odd


def maybe_double_last(hand):
    return hand[:-1] + [22] if hand[-1] == 11 else hand


print(average_even_is_average_odd([1, 3, 5, 7, 9]))
