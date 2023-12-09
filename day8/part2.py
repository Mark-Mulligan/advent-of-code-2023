import re
import math


class Solution():
    def __init__(self, file_path):
        self.file_path = file_path
        self.path_instructions = []
        self.adjancey_list = {}
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for i, line in enumerate(input):
                formatted_line = line.strip()

                if i == 0:
                    self.path_instructions = list(formatted_line)
                elif formatted_line:
                    [item, paths] = [item.strip()
                                     for item in formatted_line.split('=')]
                    cleaned_paths = [path.strip() for path in re.sub(
                        r'\(|\)', '', paths).split(',')]

                    self.adjancey_list[item] = cleaned_paths

    def check_if_all_paths_finished(self, all_paths):
        for path in all_paths:
            if path[-1] != 'Z':
                return False

        return True

    def traverse_map(self):
        current_paths = []
        for item in self.adjancey_list:
            if item[-1] == 'A':
                current_paths.append(item)

        nums = []
        for path in current_paths:
            current_path = path
            path_i = 0
            steps = 0

            while current_path[-1] != 'Z':
                if self.path_instructions[path_i] == 'R':
                    current_path = self.adjancey_list[current_path][1]
                else:
                    current_path = self.adjancey_list[current_path][0]

                steps += 1
                if path_i < len(self.path_instructions) - 1:
                    path_i += 1
                else:
                    path_i = 0

            nums.append(steps)

        return nums


solution = Solution('./input_day8.txt')
nums = solution.traverse_map()
print(math.lcm(*nums))
