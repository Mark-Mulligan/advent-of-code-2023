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
                self.marked_matrix.append(row)

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
    
    def check_up_left(self, x, y):
        pipe_count = 0

        while x > 0 and y > 0:
            x -= 1
            y -= 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if found_pipe:
                pipe_count += 1
        
        return pipe_count

    def check_up_right(self, x, y):
        pipe_count = 0

        while x > 0 and y < len(self.matrix[x]) - 1:
            x -= 1
            y += 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if found_pipe:
                pipe_count += 1
        
        return pipe_count
    
    def check_down_left(self, x, y):
        pipe_count = 0

        while x < len(self.matrix) - 1 and y > 0:
            x += 1
            y -= 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            
            if found_pipe:
                pipe_count += 1
        
        return pipe_count
    
    def check_down_right(self, x, y):
        pipe_count = 0

        while x < len(self.matrix) - 1 and y < len(self.marked_matrix[x]) - 1:
            x += 1
            y += 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if found_pipe:
                pipe_count += 1
        
        return pipe_count


    def check_left(self, x, y):
        pipe_count = 0

        while y > 0:
            y -= 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if found_pipe and found_pipe in ['|', 'J', 'L', 'F', '7']:
                pipe_count += 1

        return pipe_count
    
    def check_right(self, x, y):
        pipe_count = 0
        

        while y < len(self.matrix[x]) - 1:
            y += 1

            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if found_pipe and found_pipe in ['|', 'J', 'L', 'F', '7']:
                pipe_count += 1
            
        return pipe_count
    
    def check_up(self, x, y):
        pipe_count = 0
        
        while x > 0:
            x -= 1
        
            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if found_pipe and found_pipe in ['-', 'J', 'L', 'F', '7']:
                pipe_count += 1
        
        return pipe_count
    
    def check_down(self, x, y):
        pipe_count = 0
        
        while x < len(self.matrix) - 1:
            x += 1
        
            found_pipe = self.matrix_hash.get(f"{x}-{y}")
            if found_pipe and found_pipe in ['-', 'J', 'L', 'F', '7']:
                pipe_count += 1
        
        return pipe_count
    
    def check_tile(self, x, y):
        if f"{x}-{y}" not in self.matrix_hash:
            left_pipe_count = self.check_left(x, y)
            right_pipe_count = self.check_right(x, y)
            up_pipe_count = self.check_up(x, y)
            down_pipe_count = self.check_down(x, y)
            pipe_counts = [left_pipe_count, right_pipe_count, up_pipe_count, down_pipe_count]

            up_left_pipe_count = self.check_up_left(x, y)
            up_right_pipe_count = self.check_up_right(x, y)
            down_left_pipe_count = self.check_down_left(x, y)
            down_right_pipe_count = self.check_down_right(x, y)
            diag_pipe_counts = [up_left_pipe_count, up_right_pipe_count, down_left_pipe_count, down_right_pipe_count]

            if x == 4 and y == 7:
                print(pipe_counts)
                print(diag_pipe_counts)
                
            if 0 in pipe_counts or 0 in diag_pipe_counts:
                self.marked_matrix[x][y] = 'O'
                return False
            
            for count in pipe_counts:
                if count % 2 != 0:
                    return True
                
            self.marked_matrix[x][y] = 'O'
            return False
            
        return False

    def count_surrounded_tiles(self):
        count = 0
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.check_tile(r, c):
                    self.marked_matrix[r][c] = 'I'
                    count += 1
             
        return count


solution = Solution('./input_day10.txt')
solution.check_paths()
answer = solution.count_surrounded_tiles()
print(answer)
# pprint(solution.marked_matrix, width=1200)

# 597 too high
# 580 too high
