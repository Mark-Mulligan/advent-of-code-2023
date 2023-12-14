from pprint import pprint

# Notes

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


class Solution():
    def __init__(self, file_path):
        self.file_path = file_path
        self.matrix = []
        self.matrix_hash = {}
        self.marked_matrix = []
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                row = list(line.strip())
                self.matrix.append(row)

                temp_matrix = []
                for item in row:
                    temp_matrix.append('.')
                self.marked_matrix.append(temp_matrix)

        print(self.marked_matrix)

    def find_starting_point(self):
        for r_index, r_value in enumerate(self.matrix):
            for c_index, c_value in enumerate(r_value):
                if c_value == 'S':
                    return {'x': r_index, 'y': c_index}

    def check_paths(self):
        cords = self.find_starting_point()
        matrix = self.matrix
        next_direction = 'right'
        steps = 0
        x = cords['x']
        y = cords['y']

        while next_direction:
            steps += 1
            self.matrix_hash[f"{x}-{y}"] = matrix[x][y]
            if next_direction == 'up':
                x = x - 1

                if matrix[x][y] == '|':
                    next_direction == 'up'
                elif matrix[x][y] == '7':
                    next_direction = 'left'
                elif matrix[x][y] == 'F':
                    next_direction = 'right'
            elif next_direction == 'down':
                x = x + 1

                if matrix[x][y] == '|':
                    next_direction == 'down'
                elif matrix[x][y] == 'J':
                    next_direction = 'left'
                elif matrix[x][y] == 'L':
                    next_direction = 'right'
            elif next_direction == 'left':
                y = y - 1

                if matrix[x][y] == '-':
                    next_direction = 'left'

                elif matrix[x][y] == 'L':
                    next_direction = 'up'

                elif matrix[x][y] == 'F':
                    next_direction = 'down'
            elif next_direction == 'right':
                y = y + 1

                if matrix[x][y] == '-':
                    next_direction = 'right'
                elif matrix[x][y] == '7':
                    next_direction = 'down'
                elif matrix[x][y] == 'J':
                    next_direction = 'up'
            if matrix[x][y] == 'S':
                break

        return steps

    def check_left(self, x, y):
        pipe_count = 0
        open_pipe = ''

        while y > 0:
            y -= 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if not found_pipe:
                continue

            if found_pipe in ['J', '7', 'F', 'L'] and not open_pipe:
                open_pipe = found_pipe

            if open_pipe == 'J' and found_pipe in ['F', 'L']:
                if found_pipe == 'F':
                    pipe_count += 1
                open_pipe = ''
            elif open_pipe == '7' and found_pipe in ['L', 'F']:
                if found_pipe == 'L':
                    pipe_count += 1
                open_pipe = ''
            elif open_pipe == 'F' and found_pipe in ['J', '7']:
                if found_pipe == 'J':
                    pipe_count += 1
                open_pipe = ''
            elif open_pipe == 'L' and found_pipe in ['J', '7']:
                if found_pipe == '7':
                    pipe_count += 1
                open_pipe = ''
            elif found_pipe == '|':
                pipe_count += 1

        return pipe_count

    def check_right(self, x, y):
        pipe_count = 0
        open_pipe = ''

        while y < len(self.matrix[x]) - 1:
            y += 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if not found_pipe:
                continue

            if found_pipe in ['F', 'L', 'J', '7'] and not open_pipe:
                open_pipe = found_pipe
            elif open_pipe == 'F' and found_pipe in ['J', '7']:
                if found_pipe == 'J':
                    pipe_count += 1
                open_pipe = ''
            elif open_pipe == 'L' and found_pipe in ['7', 'J']:
                if found_pipe == '7':
                    pipe_count += 1
                open_pipe = ''
            elif open_pipe == 'J' and found_pipe in ['F', 'L']:
                if found_pipe == 'F':
                    pipe_count += 1
                open_pipe = ''
            elif open_pipe == '7' and found_pipe in ['F', 'L']:
                if found_pipe == 'L':
                    pipe_count += 1
                open_pipe = ''
            elif found_pipe == '|':
                pipe_count += 1

        return pipe_count

    def check_up(self, x, y):
        pipe_count = 0
        open_pipe = ''

        while x > 0:
            x -= 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if not found_pipe:
                continue

            if found_pipe in ['J', 'L'] and not open_pipe:
                open_pipe = found_pipe
            elif open_pipe == 'J' and found_pipe in ['F', '7']:
                if found_pipe == 'F':
                    pipe_count += 1
                open_pipe = ''
            elif open_pipe == 'L' and found_pipe in ['7', 'F']:
                if found_pipe == '7':
                    pipe_count += 1
                open_pipe = ''
            elif found_pipe == '-':
                pipe_count += 1

        return pipe_count

    def check_down(self, x, y):
        pipe_count = 0
        open_pipe = ''

        while x < len(self.matrix) - 1:
            x += 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if not found_pipe:
                continue

            if found_pipe in ['F', '7']:
                open_pipe = found_pipe

            elif open_pipe == 'F' and found_pipe in ['J', 'L']:
                if found_pipe == 'J':
                    pipe_count += 1
                open_pipe = ''

            elif open_pipe == '7' and found_pipe in ['J', 'L']:
                if found_pipe == 'L':
                    pipe_count += 1
                open_pipe = ''

            elif found_pipe == '-':
                pipe_count += 1

        return pipe_count

    def check_tile(self, x, y):
        if f"{x}-{y}" not in self.matrix_hash:
            left_pipe_count = self.check_left(x, y)
            right_pipe_count = self.check_right(x, y)
            up_pipe_count = self.check_up(x, y)
            down_pipe_count = self.check_down(x, y)
            pipe_counts = [left_pipe_count, right_pipe_count,
                           up_pipe_count, down_pipe_count]

            if 0 in pipe_counts:
                return False

            for count in pipe_counts:
                if count % 2 != 0:
                    return True

            return False

        return False

    def created_clean_matrix(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if f"{r}-{c}" in self.matrix_hash:
                    self.marked_matrix[r][c] = self.matrix[r][c]
                else:
                    self.marked_matrix[r][c] = '.'

    def find_starting_cords(self):
        for r in range(len(self.marked_matrix)):
            for c in range(len(self.marked_matrix[r])):
                if self.marked_matrix[r][c] == 'S':
                    return [r, c]

    def replace_start_pipe(self):
        [x, y] = self.find_starting_cords()

        m = self.marked_matrix
        direction_to_connect = {'right': False,
                                'left': False, 'up': False, 'down': False}

        if y + 1 < len(m[0]) and m[x][y + 1] in ['-', '7', 'J']:
            direction_to_connect['right'] = True

        if y - 1 >= 0 and m[x][y - 1] in ['-', 'F', 'L']:
            direction_to_connect['left'] = True

        if x + 1 < len(m) and m[x + 1][y] in ['|', 'L', 'J']:
            direction_to_connect['down'] = True

        if x - 1 >= 0 and m[x - 1][y] in ['|', 'F', '7']:
            direction_to_connect['up'] = True

        if direction_to_connect['right'] and direction_to_connect['down']:
            self.marked_matrix[x][y] = 'F'
        elif direction_to_connect['right'] and direction_to_connect['up']:
            self.marked_matrix[x][y] = 'L'
        elif direction_to_connect['right'] and direction_to_connect['left']:
            self.marked_matrix[x][y] = '-'
        elif direction_to_connect['left'] and direction_to_connect['down']:
            self.marked_matrix[x][y] = '7'
        elif direction_to_connect['left'] and direction_to_connect['up']:
            self.marked_matrix[x][y] = 'J'
        elif direction_to_connect['up'] and direction_to_connect['down']:
            self.marked_matrix[x][y] = '|'

    def count_surrounded_tiles(self):
        count = 0
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.check_tile(r, c):
                    self.marked_matrix[r][c] = 'X'
                    count += 1

        return count


solution = Solution('./input_day10.txt')
solution.check_paths()
solution.created_clean_matrix()
solution.replace_start_pipe()
answer = solution.count_surrounded_tiles()
print(answer)

file_str = ''
for row in solution.marked_matrix:
    row_str = "".join(row) + '\n'
    file_str += row_str

f = open("matrix.txt", "w")
f.write(file_str)
f.close()
# pprint(solution.marked_matrix, width=120)

# answer = solution.count_surrounded_tiles()
# print(answer)
# pprint(solution.marked_matrix, width=1200)

# 597 too high
# 580 too high
# 366 too high
# 364 wrong
# 179 wrong
# 129 wrong

# Solution is 337
