def saddle_points(matrix):
    if len(matrix) > 0 and not len({len(row) for row in matrix}) == 1:
        raise ValueError("irregular matrix")
    points = []
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            column = [r[j] for r in matrix]
            cell = matrix[i][j]
            if all(cell >= element for element in row) and all(cell <= element for element in column):
                points.append({"row": i + 1, "column": j + 1})
    return points
