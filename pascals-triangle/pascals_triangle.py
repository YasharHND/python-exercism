def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    previous_rows = rows(row_count - 1)
    if not previous_rows:
        return [[1]]
    this_row = []
    last_idx = len(previous_rows[-1])
    for i in range(last_idx + 1):
        if i == 0 or i == last_idx:
            this_row.append(1)
        else:
            this_row.append(previous_rows[-1][i - 1] + previous_rows[-1][i])
    return previous_rows + [this_row]
