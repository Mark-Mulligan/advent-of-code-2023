from pprint import pprint
from itertools import combinations

galaxy_matrix = []

with open('./input_day11.txt') as input:
    for line in input:
        row = list(line.strip())
        galaxy_matrix.append(row)


def get_galaxy_cords(matrix):
    matrix_cords = {}
    point = 1

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == '#':
                matrix_cords[point] = [r, c]
                point += 1

    return matrix_cords


def find_empty_rows(orginal_matrix):
    empty_rows = []
    for r, row in enumerate(orginal_matrix):
        if '#' not in row:
            empty_rows.append(r)

    return empty_rows


def find_empty_columns(matrix):
    empty_columns = []

    for c in range(len(matrix[0])):
        hash_found = False
        for r in range(len(matrix)):
            if matrix[r][c] == '#':
                hash_found = True

        if not hash_found:
            empty_columns.append(c)

    return empty_columns


def calc_diffs(matrix_cords, empty_rows, empty_columns, expansion):
    point_combinations = list(combinations([cord for cord in matrix_cords], 2))
    total = 0

    for c in point_combinations:
        empty_rows_crossed = 0
        empty_cols_crossed = 0

        x1 = matrix_cords[c[0]][0]
        x2 = matrix_cords[c[1]][0]
        y1 = matrix_cords[c[0]][1]
        y2 = matrix_cords[c[1]][1]

        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        for r in empty_rows:
            if min_x < r and max_x > r:
                empty_rows_crossed += expansion - 1

        for c in empty_columns:
            if min_y < c and max_y > c:
                empty_cols_crossed += expansion - 1

        distance_x = abs(x1 - x2)
        distance_y = abs(y1 - y2)
        distance = distance_x + distance_y
        total += distance + empty_rows_crossed + empty_cols_crossed

    return total


pprint(galaxy_matrix)
galaxy_cords = get_galaxy_cords(galaxy_matrix)
print(galaxy_cords)
empty_rows = find_empty_rows(galaxy_matrix)
empty_columns = find_empty_columns(galaxy_matrix)
answer = calc_diffs(galaxy_cords, empty_rows, empty_columns, 1000000)
print(answer)
