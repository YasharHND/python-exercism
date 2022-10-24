def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_rate += (spread / 100) * exchange_rate
    budget /= exchange_rate
    return (budget // denomination) * denomination


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_rate += (spread / 100) * exchange_rate
    new_budget = budget / exchange_rate
    return int(new_budget - ((new_budget // denomination) * denomination))
