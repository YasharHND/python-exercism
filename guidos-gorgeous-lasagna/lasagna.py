EXPECTED_BAKE_TIME = 40
LAYER_PREPARATION_TIME = 2


def bake_time_remaining(minutes):
    """
    This is something
    :param minutes:
    :return:
    """
    return EXPECTED_BAKE_TIME - minutes


def preparation_time_in_minutes(count):
    """
    This is something
    :param count:
    :return:
    """
    return LAYER_PREPARATION_TIME * count


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    This is something
    :param number_of_layers:
    :param elapsed_bake_time:
    :return:
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


print(elapsed_time_in_minutes(3, 20))

