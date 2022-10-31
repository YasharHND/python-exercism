def total(basket):
    if len(basket) == 0:
        return 0
    basket.sort()
    fair_division_sets = []
    for book in basket:
        min_length = min([len(i) for i in fair_division_sets if book not in i], default=0)
        for item in fair_division_sets:
            if len(item) == min_length and book not in item:
                item.append(book)
                break
        else:
            fair_division_sets.append([book])
    if is_set_of_each_size(fair_division_sets):
        fair_division_sets.sort()
        book_to_move = fair_division_sets[0].pop()
        fair_division_sets[2].append(book_to_move)
        return calculate_basket_price(fair_division_sets)
    greedy_sets = []
    for book in basket:
        for book_set in greedy_sets:
            if book not in book_set:
                book_set.append(book)
                break
        else:
            greedy_sets.append([book])
    return min(calculate_basket_price(fair_division_sets), calculate_basket_price(greedy_sets))


def is_set_of_each_size(sets):
    sets.sort()
    i = 5
    for book_set in sets:
        if len(book_set) != i or i == 0:
            return False
        i -= 1
    return i == 0


def calculate_basket_price(sets):
    price = 0
    for book_set in sets:
        count = len(book_set)
        set_price = count * 800
        if count > 1:
            discount_percentage = 25 if count == 5 else (2 ** (count - 2)) * 5
            set_price -= int(set_price * (discount_percentage / 100))
        price += set_price
    return price
