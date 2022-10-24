def rstrip_until(row, till):
    out = row.rstrip()
    if len(out) < till:
        out += "".join([" " for _ in range(till - len(out))])
    return out


def transpose(lines):
    if len(lines) == 0:
        return ""
    lines_split = lines.split("\n")
    length = max([len(line) for line in lines_split])
    lines_clean = []
    for line in lines_split:
        lines_clean.append(line + "".join([" " for _ in range(length - len(line))]))
    rows = []
    for i in range(length):
        row = "".join([line[i] for line in lines_clean])
        rows.append(row)
    rows_cleaned = []
    last_row_length = 0
    for row in reversed(rows):
        new_row = rstrip_until(row, last_row_length) if len(row) > last_row_length else row
        rows_cleaned.insert(0, new_row)
        last_row_length = len(new_row)
    for row in rows_cleaned:
        print(">>>" + row + "<<<")
    return "\n".join(rows_cleaned)


transpose("\n".join(["The longest line.", "A long line.", "A longer line.", "A line."]))
