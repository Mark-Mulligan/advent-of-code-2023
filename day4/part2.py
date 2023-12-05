from collections import Counter
from pprint import pprint


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.total_cards = 0
        self.card_scores = {}
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for i, line in enumerate(input):
                [card, winning_nums] = [
                    item.strip() for item in line.split(":")[1].strip().split("|")
                ]

                card_hash = Counter(card.split(" "))
                winning_nums = winning_nums.replace("  ", " ").split(" ")
                matches = 0
                for num in winning_nums:
                    if num in card_hash:
                        matches += card_hash[num]

                self.card_scores[i + 1] = {"card_count": 1, "matches": int(matches)}

    def calc_total_matches(self):
        for match in self.card_scores:
            for card in range(self.card_scores[match]["card_count"]):
                for m in range(1, self.card_scores[match]["matches"] + 1):
                    self.card_scores[match + m]["card_count"] += 1

        for card in self.card_scores:
            self.total_cards += self.card_scores[card]["card_count"]


solution = Solution("input_day4.txt")

solution.calc_total_matches()
pprint(solution.card_scores)
print(solution.total_cards)
