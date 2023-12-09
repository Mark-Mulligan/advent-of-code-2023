import re


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

    def traverse_map(self):
        current_path = 'AAA'
        path_i = 0
        steps = 0

        while current_path != 'ZZZ':
            if self.path_instructions[path_i] == 'R':
                current_path = self.adjancey_list[current_path][1]
            else:
                current_path = self.adjancey_list[current_path][0]

            steps += 1
            if path_i < len(self.path_instructions) - 1:
                path_i += 1
            else:
                path_i = 0

        return steps


solution = Solution('./input_day8.txt')
print(solution.path_instructions)
print(solution.adjancey_list)
steps = solution.traverse_map()
print(steps)
