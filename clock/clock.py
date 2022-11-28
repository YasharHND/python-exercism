class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.recalibrate()

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:0>2}:{self.minute:0>2}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute += minutes
        self.recalibrate()
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.recalibrate()
        return self

    def recalibrate(self):
        if not 0 <= self.minute < 60:
            self.hour += self.minute // 60
            self.minute = abs(self.minute % 60)
        if not 0 <= self.hour < 24:
            self.hour = abs(self.hour % 24)
