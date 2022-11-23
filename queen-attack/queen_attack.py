class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.row == another_queen.row:
            return True
        if self.column == another_queen.column:
            return True

        def can_attack_lr(w, b):
            row = w.row - w.column
            column = 0
            while True:
                if b.row == row and b.column == column:
                    return True
                row += 1
                column += 1
                if row > 7 or column > 7:
                    return False

        def can_attack_rl(w, b):
            row = w.row + w.column
            column = 0
            while True:
                print(row, column)
                if b.row == row and b.column == column:
                    return True
                row -= 1
                column += 1
                if row < 0 or column > 7:
                    return False

        return can_attack_lr(self, another_queen) or can_attack_rl(self, another_queen)
