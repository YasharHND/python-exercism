def make_board(message, rails):
    board = [[] for _ in range(rails)]
    i = 0
    d = +1
    for char in message:
        board[i].append(char)
        if d == +1 and i == rails - 1:
            d = -1
        elif d == -1 and i == 0:
            d = +1
        i += d
    return board


def encode(message, rails):
    board = make_board(message, rails)
    out = ""
    for rail in board:
        out += "".join(rail)
    return out


def decode(encoded_message, rails):
    dummy_board = make_board(encoded_message, rails)
    board = []
    last_idx = 0
    for i in range(rails):
        this_idx = len(dummy_board[i])
        new_end = last_idx + this_idx
        board.append(encoded_message[last_idx:new_end])
        last_idx = new_end
    indices = {}
    for i in range(rails):
        indices.update({i: 0})
    out = ""
    i = 0
    d = +1
    for _ in range(len(encoded_message)):
        out += board[i][indices[i]]
        indices[i] += 1
        if d == +1 and i == rails - 1:
            d = -1
        elif d == -1 and i == 0:
            d = +1
        i += d
    return out
