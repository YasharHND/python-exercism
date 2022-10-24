def can_chain(dominoes):
    if len(dominoes) == 0:
        return []
    return chain([], dominoes, len(dominoes))


def chain(snake, pile, expected_length):
    options = pile if len(snake) == 0 else [i for i in pile if i[0] == snake[-1][1] or i[1] == snake[-1][1]]
    for item in options:
        next_item = item if len(snake) == 0 or item[0] == snake[-1][1] else tuple((item[1], item[0]))
        new_snake = snake + [next_item]
        if is_completed(new_snake, expected_length):
            return new_snake
        i = pile.index(item)
        new_pile = pile[1:] if i == 0 else pile[:-1] if i == len(pile) - 1 else pile[:i] + pile[i + 1:]
        final_snake = chain(new_snake, new_pile, expected_length)
        if final_snake is not None and is_completed(final_snake, expected_length):
            return final_snake


def is_completed(snake, expected_length):
    return len(snake) == expected_length and snake[0][0] == snake[-1][1]
