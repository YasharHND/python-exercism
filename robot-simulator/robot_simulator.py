EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4

rotate_r = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

rotate_l = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH
}

advance = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0)
}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, steps):
        for step in steps:
            if step == "A":
                diff = advance.get(self.direction)
                self.coordinates = (self.coordinates[0] + diff[0], self.coordinates[1] + diff[1])
            else:
                self.direction = rotate_r.get(self.direction) if step == "R" else rotate_l.get(self.direction)
