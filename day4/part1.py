from collections import Counter
import math


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.total_score = 0
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                [card, winning_nums] = [
                    item.strip() for item in line.split(":")[1].strip().split("|")
                ]

                card_hash = Counter(card.split(" "))
                winning_nums = winning_nums.replace("  ", " ").split(" ")
                matches = 0
                for num in winning_nums:
                    if num in card_hash:
                        matches += card_hash[num]

                card_score = 0
                if matches - 1 >= 0:
                    card_score = math.pow(2, matches - 1)

                self.total_score += int(card_score)


solution = Solution("input_day4.txt")
print(solution.total_score)
