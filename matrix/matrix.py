class Matrix:
    def __init__(self, matrix_string):
        self.grid = [[int(n) for n in line.split(" ")] for line in matrix_string.split("\n")]

    def row(self, index):
        return self.grid[index - 1]

    def column(self, index):
        return [line[index - 1] for line in self.grid]
