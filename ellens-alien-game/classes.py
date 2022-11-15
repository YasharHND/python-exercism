class Alien:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created = Alien.total_aliens_created + 1 if hasattr(Alien, 'total_aliens_created') else 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
        pass


def new_aliens_collection(positions):
    return [Alien(position[0], position[1]) for position in positions]
