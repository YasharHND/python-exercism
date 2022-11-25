def all_lines(strings, tl, tr, br, bl):
    if any(char in (" ", "|") for char in strings[tl[0]][tl[1] + 1:tr[1]]):
        return False
    if any(char in (" ", "|") for char in strings[bl[0]][bl[1] + 1:br[1]]):
        return False
    if any(line[tl[1]] in (" ", "-") for line in strings[tl[0] + 1:bl[0]]):
        return False
    if any(line[tr[1]] in (" ", "-") for line in strings[tr[0] + 1:br[0]]):
        return False
    return True


def rectangles(strings):
    count = 0
    lines = len(strings)
    for row in range(lines):
        for column in range(len(strings[0])):
            char = strings[row][column]
            if char == "+" and row < lines - 1:
                tl = row, column
                top_right_points = [column + i + 1 for i, that_char in enumerate(strings[row][column + 1:]) if that_char == "+"]
                for tr_point in top_right_points:
                    tr = row, tr_point
                    bottom_right_points = [row + i + 1 for i, line in enumerate(strings[row + 1:]) if line[tr_point] == "+"]
                    for br_point in bottom_right_points:
                        br = br_point, tr[1]
                        bl = (br[0], tl[1]) if strings[br[0]][tl[1]] == "+" else None
                        if bl and all_lines(strings, tl, tr, br, bl):
                            count += 1

    return count
