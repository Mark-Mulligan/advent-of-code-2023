from collections import Counter
from pprint import pprint


class Solution():
    def __init__(self, file_path):
        self.file_path = file_path
        self.card_values = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2,
            '1': 1
        }
        self.winnings = 0
        self.cards = []
        self.read_input()
        self.calc_answer()

    def get_card_score(self, card_counts):
        if 5 in card_counts.values():
            return 7
        if 4 in card_counts.values():
            return 6
        if 3 in card_counts.values() and 2 in card_counts.values():
            return 5
        if 3 in card_counts.values():
            return 4
        if len(card_counts) == 3 and 2 in card_counts.values():
            return 3
        if 2 in card_counts.values():
            return 2

        return 1

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                formatted_line = line.strip()
                [hand, bet] = formatted_line.split(' ')
                card_counts = Counter(hand)
                score = self.get_card_score(card_counts)
                card_scores = [self.card_values[card] for card in hand]
                self.cards.append(
                    {"hand": hand, "bet": int(bet), "score": score, "card_scores": card_scores})

    def calc_answer(self):
        cards = sorted(self.cards, key=lambda a: (
            a['score'], a['card_scores']))

        for i, card in enumerate(cards):
            self.winnings += card['bet'] * (i + 1)


solution = Solution('./input_day7.txt')
print(solution.winnings)
