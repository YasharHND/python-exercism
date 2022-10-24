def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500_000


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = ((voltage * current) / theoretical_max_power) * 100
    return (
        "green" if generated_power >= 80
        else "orange" if 60 <= generated_power < 80
        else "red" if 30 <= generated_power < 60
        else "black"
    )


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < percentage(90, threshold):
        return "LOW"
    elif 0 <= abs(threshold - (temperature * neutrons_produced_per_second)) <= percentage(10, threshold):
        return "NORMAL"
    else:
        return "DANGER"


def percentage(percent, whole):
    return (percent * whole) / 100.0
