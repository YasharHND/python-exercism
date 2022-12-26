def get_extra_hours(hours):
    return (hours + 3) % 24


def get_kW_amount(watts):
    return round(watts / 1000, 1)


def get_kwh_amount(watts):
    return (watts / 1000) // 3600


def get_efficiency(power_factor):
    return power_factor / 100


def get_cost(watts, power_factor, price):
    power_used = get_kwh_amount(watts) / get_efficiency(power_factor)
    if power_used == 0:
        return 0
    return price * power_used
