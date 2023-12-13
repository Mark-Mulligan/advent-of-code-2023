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
        self.marked_matrix = []
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                row = list(line.strip())
                self.matrix.append(row)
                self.marked_matrix.append(['.' for item in row])

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
            self.marked_matrix[x][y] = 'X'
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

    
    def check_left(self, x, y):
        matrix = self.marked_matrix
        x_count = 0

        while y > 0:
            y -= 1

            if matrix[x][y] == 'X':
                x_count += 1

        return x_count
    
    def check_right(self, x, y):
        matrix = self.marked_matrix
        x_count = 0

        while y < len(self.marked_matrix[x]) - 2:
            y += 1

            if matrix[x][y] == 'X':
                x_count += 1
            
        return x_count
    
    def check_up(self, x, y):
        matrix = self.marked_matrix
        x_count = 0
        
        while x > 0:
            x -= 1
        
            if matrix[x][y] == 'X':
                x_count += 1
        
        return x_count
    
    def check_down(self, x, y):
        matrix = self.marked_matrix
        x_count = 0
        
        while x < len(self.marked_matrix) - 2:
            x += 1
        
            if matrix[x][y] == 'X':
                x_count += 1
        
        return x_count
    
    def check_tile(self, x, y):
        matrix = self.marked_matrix

        if matrix[x][y] != 'X':
            left_x_count = self.check_left(x, y)
            right_x_count = self.check_right(x, y)
            up_x_count = self.check_up(x, y)
            down_x_count = self.check_down(x, y)
            x_counts = [left_x_count, right_x_count, up_x_count, down_x_count]

            if 0 in x_counts:
                return False

            for count in x_counts:
                if count % 2 != 0:
                    return True
            
            return False
        
        return False
    
    def mark_tiles(self):
        matrix = self.marked_matrix

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] != 'X' and self.check_tile(r, c):
                    matrix[r][c] = 'O'

    def count_surrounded_tiles(self):
        count = 0

        for r in range(len(self.marked_matrix)):
            for c in range(len(self.marked_matrix[r])):
                if self.marked_matrix[r][c] == 'O':
                    count += 1
        
        return count

solution = Solution('./test_input3.txt')
solution.check_paths()
pprint(solution.marked_matrix, width=120)
solution.mark_tiles()
answer = solution.count_surrounded_tiles()
pprint(solution.marked_matrix, width=120)
print(answer)

