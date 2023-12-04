import re


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.engine_matrix = []
        self.gear_ratios = []
        self.gear_ratio_total = 0
        self.load_input()

    def load_input(self):
        with open(self.file_path) as input:
            for line in input:
                formatted_line = line.strip()
                self.engine_matrix.append(list(formatted_line))

    def get_full_num(self, num, x, y):
        matrix = self.engine_matrix
        num_pattern = re.compile(r"[0-9]")
        r = y
        left = y

        while left > 0 and True:
            left -= 1
            if num_pattern.match(matrix[x][left]):
                num = f"{matrix[x][left]}{num}"
            else:
                break

        while r < len(matrix[x]) - 1 and True:
            r += 1
            if num_pattern.match(matrix[x][r]):
                num = f"{num}{matrix[x][r]}"
            else:
                break

        return num

    def check_engine_gear(self, x, y, matrix):
        num_pattern = re.compile(r"[0-9]")
        found_nums = set()

        if x - 1 >= 0 and y - 1 >= 0 and num_pattern.match(matrix[x - 1][y - 1]):
            found_num = self.get_full_num(matrix[x - 1][y - 1], x - 1, y - 1)
            found_nums.add(found_num)

        if x - 1 >= 0 and num_pattern.match(matrix[x - 1][y]):
            found_num = self.get_full_num(matrix[x - 1][y], x - 1, y)
            found_nums.add(found_num)

        if (
            x - 1 >= 0
            and y + 1 < len(matrix[x])
            and num_pattern.match(matrix[x - 1][y + 1])
        ):
            found_num = self.get_full_num(matrix[x - 1][y + 1], x - 1, y + 1)
            found_nums.add(found_num)

        if y - 1 >= 0 and num_pattern.match(matrix[x][y - 1]):
            found_num = self.get_full_num(matrix[x][y - 1], x, y - 1)
            found_nums.add(found_num)

        if y + 1 >= 0 and num_pattern.match(matrix[x][y + 1]):
            found_num = self.get_full_num(matrix[x][y + 1], x, y + 1)
            found_nums.add(found_num)

        if (
            x + 1 < len(matrix)
            and y - 1 >= 0
            and num_pattern.match(matrix[x + 1][y - 1])
        ):
            found_num = self.get_full_num(matrix[x + 1][y - 1], x + 1, y - 1)
            found_nums.add(found_num)

        if x + 1 < len(matrix) and num_pattern.match(matrix[x + 1][y]):
            found_num = self.get_full_num(matrix[x + 1][y], x + 1, y)
            found_nums.add(found_num)

        if (
            x + 1 < len(matrix)
            and y + 1 < len(matrix[x])
            and num_pattern.match(matrix[x + 1][y + 1])
        ):
            found_num = self.get_full_num(matrix[x + 1][y + 1], x + 1, y + 1)
            found_nums.add(found_num)

        return found_nums

    def find_engine_gears(self):
        for r in range(len(self.engine_matrix)):
            for c in range(len(self.engine_matrix[r])):
                char = self.engine_matrix[r][c]

                if char == "*":
                    found_nums = self.check_engine_gear(r, c, self.engine_matrix)

                    if len(found_nums) == 2:
                        gear_ratio = 1
                        for num in found_nums:
                            gear_ratio *= int(num)
                        self.gear_ratios.append(gear_ratio)
                        self.gear_ratio_total += gear_ratio


solution = Solution("./input_day3.txt")
solution.find_engine_gears()
print(solution.gear_ratios)
print(solution.gear_ratio_total)
