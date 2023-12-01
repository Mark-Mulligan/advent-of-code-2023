import functools


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.numbers = []
        self.digit_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        self.load_input()

    def load_input(self):
        with open(self.file_path) as input:
            for i, line in enumerate(input):
                formatted_line = line.strip()
                digit_hash = {}

                for word in self.digit_map.keys():
                    if word in formatted_line:
                        first_index = formatted_line.index(word)
                        digit_hash[first_index] = self.digit_map[word]
                        last_index = formatted_line.rindex(word)
                        digit_hash[last_index] = self.digit_map[word]

                for digit in self.digit_map.values():
                    if digit in formatted_line:
                        first_index = formatted_line.index(digit)
                        digit_hash[first_index] = digit
                        last_index = formatted_line.rindex(digit)
                        digit_hash[last_index] = digit

                first_digit_index = min(digit_hash.keys())
                last_digit_index = max(digit_hash.keys())
                first_digit = digit_hash[first_digit_index]
                last_digit = digit_hash[last_digit_index]
                self.numbers.append(int(f"{first_digit}{last_digit}"))

    def get_answer(self):
        return functools.reduce(lambda a, b: a + b, self.numbers)


solution = Solution("./day_input.txt")
answer = solution.get_answer()
print(solution.numbers[600])
print(answer)
