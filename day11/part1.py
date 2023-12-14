from pprint import pprint
from itertools import combinations

galaxy_matrix = []

with open('./test_input.txt') as input:
    for line in input:
        row = list(line.strip())
        galaxy_matrix.append(row)


def add_extra_rows(orginal_matrix):
    new_matrix = []
    for row in orginal_matrix:
        new_matrix.append(row)
        if '#' not in row:
            new_matrix.append(row)

    return new_matrix


def add_extra_columns(matrix):
    matrix_base = [[] for _ in matrix]

    for c in range(len(matrix[0])):
        hash_found = False
        for r in range(len(matrix)):
            if matrix[r][c] == '#':
                hash_found = True
            matrix_base[r].append(matrix[r][c])

        if not hash_found:
            for r in range(len(matrix)):
                matrix_base[r].append('.')

    return matrix_base


def get_galaxy_cords(matrix):
    matrix_cords = {}
    point = 1

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == '#':
                matrix_cords[point] = [r, c]
                point += 1

    return matrix_cords


def calc_diffs(matrix_cords):
    point_combinations = list(combinations([cord for cord in matrix_cords], 2))
    total = 0

    for c in point_combinations:
        distance_x = abs(matrix_cords[c[0]][0] - matrix_cords[c[1]][0])
        distnace_y = abs(matrix_cords[c[0]][1] - matrix_cords[c[1]][1])
        distance = distance_x + distnace_y
        total += distance

    return total


pprint(galaxy_matrix)
galaxy_matrix = add_extra_rows(galaxy_matrix)
galaxy_matrix = add_extra_columns(galaxy_matrix)
galaxy_cords = get_galaxy_cords(galaxy_matrix)
answer = calc_diffs(galaxy_cords)
print(answer)
