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
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                row = list(line.strip())
                self.matrix.append(row)

    def find_starting_point(self):
        for r_index, r_value in enumerate(self.matrix):
            for c_index, c_value in enumerate(r_value):
                if c_value == 'S':
                    return {'x': r_index, 'y': c_index}

    def check_paths(self):
        cords = self.find_starting_point()
        matrix = self.matrix
        next_direction = 'up'
        steps = 0
        x = cords['x']
        y = cords['y']

        while next_direction:
            steps += 1
            if next_direction == 'up':
                x = x - 1

                if matrix[x][y] == '|':
                    next_direction == 'up'

                if matrix[x][y] == '7':
                    next_direction = 'left'

                if matrix[x][y] == 'F':
                    next_direction = 'right'
            elif next_direction == 'down':
                x = x + 1

                if matrix[x][y] == '|':
                    next_direction == 'down'

                if matrix[x][y] == 'J':
                    next_direction = 'left'

                if matrix[x][y] == 'L':
                    next_direction = 'right'
            elif next_direction == 'left':
                y = y - 1

                if matrix[x][y] == '-':
                    next_direction = 'left'

                if matrix[x][y] == 'L':
                    next_direction = 'up'

                if matrix[x][y] == 'F':
                    next_direction = 'down'
            elif next_direction == 'right':
                y = y + 1

                if matrix[x][y] == '-':
                    next_direction = 'right'

                if matrix[x][y] == '7':
                    next_direction = 'down'

                if matrix[x][y] == 'J':
                    next_direction = 'up'

            if matrix[x][y] == 'S':
                break

        return steps


solution = Solution('./input_day10.txt')
answer = solution.check_paths()
print(answer / 2)
