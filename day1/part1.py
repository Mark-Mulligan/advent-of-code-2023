import re
import functools


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.numbers = []
        self.load_input()

    def load_input(self):
        with open(self.file_path) as input:
            for line in input:
                formatted_line = line.strip()
                digits_found = []

                for char in formatted_line:
                    num_match = re.match("[0-9]", char)
                    if num_match:
                        digits_found.append(int(char))

                num = f"{digits_found[0]}{digits_found[-1]}"
                self.numbers.append(int(num))

    def get_answer(self):
        return functools.reduce(lambda a, b: a + b, self.numbers)


solution = Solution("./day_input.txt")
print(solution.numbers)
answer = solution.get_answer()
print(answer)
