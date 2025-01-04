def check_row(matrix):
    for row in matrix:
        if row.count(0) == 1:
            index = row.index(0)
            num = {1, 2, 3, 4} - set(row)
            row[index] = num.pop()
    return matrix


def check_col(matrix):
    for c in range(4):
        column = [row[c] for row in matrix]
        if column.count(0) == 1:
            index = column.index(0)
            num = {1, 2, 3, 4} - set(column)
            matrix[index][c] = num.pop()
    return matrix


def check_square(matrix):
    square_index = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for r, c in square_index:
        square = [matrix[r][c], matrix[r][c + 1],
                  matrix[r + 1][c], matrix[r + 1][c + 1]]
        if square.count(0) == 1:
            index = square.index(0)
            num = {1, 2, 3, 4} - set(square)
            matrix[r + index // 2][c + index % 2] = num.pop()
    return matrix


def main():
    matrix = list()
    for _ in range(4):
        matrix.append([int(n) for n in input().split()])
    while not all(all(row) for row in matrix):
        for check in check_row, check_col, check_square:
            matrix = check(matrix)
    for row in matrix:
        print(row[0], row[1], row[2], row[3])


if __name__ == "__main__":
    main()
