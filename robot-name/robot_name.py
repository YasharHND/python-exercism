import random
import string

robot_names = []


def random_name():
    while True:
        name = "".join(random.choices(string.ascii_uppercase, k=2)) + str(random.randint(100, 1000))
        if name not in robot_names:
            robot_names.append(name)
            return name


class Robot:
    def __init__(self):
        self.name = random_name()

    def reset(self):
        self.name = random_name()
