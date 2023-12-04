import re


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.engine_matrix = []
        self.found_nums = []
        self.load_input()

    def load_input(self):
        with open(self.file_path) as input:
            for line in input:
                formatted_line = line.strip()
                self.engine_matrix.append(list(formatted_line))

    def look_for_adjacent_symbols(self, x, y, matrix):
        special_char = re.compile(r"[^a-zA-Z0-9\.]")

        if x - 1 >= 0 and y - 1 >= 0 and special_char.match(matrix[x - 1][y - 1]):
            return True
        if x - 1 >= 0 and special_char.match(matrix[x - 1][y]):
            return True
        if (
            x - 1 >= 0
            and y + 1 < len(matrix[x])
            and special_char.match(matrix[x - 1][y + 1])
        ):
            return True
        if y - 1 >= 0 and special_char.match(matrix[x][y - 1]):
            return True
        if y + 1 < len(matrix[x]) and special_char.match(matrix[x][y + 1]):
            return True
        if (
            x + 1 < len(matrix)
            and y - 1 >= 0
            and special_char.match(matrix[x + 1][y - 1])
        ):
            return True
        if x + 1 < len(matrix) and special_char.match(matrix[x + 1][y]):
            return True
        if (
            x + 1 < len(matrix)
            and y + 1 < len(matrix[x])
            and special_char.match(matrix[x + 1][y + 1])
        ):
            return True

        return False

    def traverse_matrix(self):
        num_pattern = re.compile(r"[0-9]")

        for r in range(len(self.engine_matrix)):
            num_sequence = ""
            adjacent_to_symbol = False

            for c in range(len(self.engine_matrix[r])):
                char = self.engine_matrix[r][c]

                if num_pattern.match(char):
                    num_sequence += char
                    adjacent_symbol = self.look_for_adjacent_symbols(
                        r, c, self.engine_matrix
                    )

                    if adjacent_symbol:
                        adjacent_to_symbol = True

                    # covers number at end of row
                    if (
                        c == len(self.engine_matrix[r]) - 1
                        and num_sequence
                        and adjacent_to_symbol
                    ):
                        self.found_nums.append(int(num_sequence))
                        adjacent_to_symbol = False
                        num_sequence = ""

                elif num_sequence and adjacent_to_symbol:
                    self.found_nums.append(int(num_sequence))
                    adjacent_to_symbol = False
                    num_sequence = ""
                else:
                    adjacent_to_symbol = False
                    num_sequence = ""

    def get_sum(self):
        result = 0

        for num in self.found_nums:
            result += int(num)

        return result

    def search_result(self, search):
        for item in self.found_nums:
            if item == search:
                return True

        return False


solution = Solution("./input_day3.txt")
solution.traverse_matrix()
print(sorted(solution.found_nums))
print(solution.get_sum())
print(solution.search_result("757"))

# 538293 too low
# Need to get 540131
# 558293 too high
