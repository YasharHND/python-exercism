numbers_map = {
    " _ | ||_|": "0",
    "     |  |": "1",
    " _  _||_ ": "2",
    " _  _| _|": "3",
    "   |_|  |": "4",
    " _ |_  _|": "5",
    " _ |_ |_|": "6",
    " _   |  |": "7",
    " _ |_||_|": "8",
    " _ |_| _|": "9"
}


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any([len(row) % 3 != 0 for row in input_grid]):
        raise ValueError("Number of input columns is not a multiple of three")
    out = ""
    prefix = ""
    rows_count = len(input_grid) // 4
    for r in range(rows_count):
        row = prefix
        digits_count = len(input_grid[r * 4]) // 3
        for d in range(digits_count):
            r_srt_idx = d * 3
            r_end_idx = (d + 1) * 3
            ocr = input_grid[r * 4][r_srt_idx:r_end_idx]
            ocr += input_grid[(r * 4) + 1][r_srt_idx:r_end_idx]
            ocr += input_grid[(r * 4) + 2][r_srt_idx:r_end_idx]
            row += numbers_map[ocr] if ocr in numbers_map else "?"
        out += row
        prefix = ","
    return out
