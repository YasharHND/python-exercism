import calendar
from datetime import date


class MeetupDayException(ValueError):
    def __init__(self, message):
        self.message = message


weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

index = {
    "first": 0,
    "second": 1,
    "third": 2,
    "fourth": 3,
    "fifth": 4,
    "last": -1
}


def nth(*args):
    occurrences = args[0]
    idx = index[args[1]]
    if idx >= len(occurrences):
        raise MeetupDayException("That day does not exist.")
    return occurrences[idx]


def teenth(*args):
    return next(i for i in args[0] if 13 <= i <= 19)


pointer = {
    "first": nth,
    "second": nth,
    "third": nth,
    "fourth": nth,
    "last": nth,
    "fifth": nth,
    "teenth": teenth
}


def meetup(year, month, week, day_of_week):
    dates = []
    first_day_of_month = date(year, month, 1)
    last_date_of_month = calendar.monthrange(year, month)[1]
    diff = (weekdays.index(day_of_week) + 1) - first_day_of_month.weekday()
    while diff <= last_date_of_month:
        if diff > 0:
            dates.append(diff)
        diff += 7
    target = pointer[week](dates, week)
    return date(year, month, target)
