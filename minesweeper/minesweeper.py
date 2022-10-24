def get_adjacent_indices(x, y, width, height):
    out = []
    if y > 0:
        if x > 0:
            out.append((x - 1, y - 1))
        out.append((x, y - 1))
        if x < width - 1:
            out.append((x + 1, y - 1))
    if x > 0:
        out.append((x - 1, y))
    if x < width - 1:
        out.append((x + 1, y))
    if y < height - 1:
        if x > 0:
            out.append((x - 1, y + 1))
        out.append((x, y + 1))
        if x < width - 1:
            out.append((x + 1, y + 1))
    return out


def annotate(minefield):
    out = []
    expected_width = len(minefield[0]) if len(minefield) > 0 else None
    height = len(minefield)
    for y in range(height):
        line = ""
        row = minefield[y]
        width = len(row)
        if width != expected_width:
            raise ValueError("The board is invalid with current input.")
        for x in range(width):
            if row[x] == " ":
                mine_count = 0
                for ax, ay in get_adjacent_indices(x, y, width, height):
                    if minefield[ay][ax] == "*":
                        mine_count += 1
                line += str(mine_count) if mine_count > 0 else " "
            elif row[x] == "*":
                line += "*"
            else:
                raise ValueError("The board is invalid with current input.")
        out.append(line)
    return out
