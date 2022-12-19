def get_next_step(board, player, path):
    i = path[-1][0]
    j = path[-1][1]
    if i > 0:
        if board[i - 1][j] == player:
            candidate = i - 1, j
            if candidate not in path:
                return candidate
        if j < len(board[0]) - 1 and board[i - 1][j + 1] == player:
            candidate = i - 1, j + 1
            if candidate not in path:
                return candidate
    if j > 0 and board[i][j - 1] == player:
        candidate = i, j - 1
        if candidate not in path:
            return candidate
    if j < len(board[0]) - 1 and board[i][j + 1] == player:
        candidate = i, j + 1
        if candidate not in path:
            return candidate
    if i < len(board) - 1:
        if j > 0 and board[i + 1][j - 1] == player:
            candidate = i + 1, j - 1
            if candidate not in path:
                return candidate
        if board[i + 1][j] == player:
            candidate = i + 1, j
            if candidate not in path:
                return candidate


def x_has_path(board):
    player = "X"
    for i, line in enumerate(board):
        if line[0] == player:
            path = [(i, 0)]
            while True:
                next_step = get_next_step(board, player, path)
                if not next_step:
                    break
                path.append(next_step)
            if path[-1][1] == len(board[0]) - 1:
                return True
    return False


def o_has_path(board):
    player = "O"
    for j, char in enumerate(board[0]):
        if char == player:
            path = [(0, j)]
            while True:
                next_step = get_next_step(board, player, path)
                if not next_step:
                    break
                path.append(next_step)
            if path[-1][0] == len(board) - 1:
                return True
    return False


class ConnectGame:
    def __init__(self, board):
        self.board = [line.replace(" ", "") for line in board.split("\n")]

    def get_winner(self):
        if x_has_path(self.board):
            return "X"
        if o_has_path(self.board):
            return "O"
        return ""
