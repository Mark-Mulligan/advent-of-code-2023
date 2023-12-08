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
            'J': 1
        }
        self.winnings = 0
        self.cards = []
        self.read_input()
        self.calc_answer()

    def get_card_score(self, card_counts):
        score = 1

        if 5 in card_counts.values():
            score = 7
        elif 4 in card_counts.values():
            score = 6
        elif 3 in card_counts.values() and 2 in card_counts.values():
            score = 5
        elif 3 in card_counts.values():
            score = 4
        elif len(card_counts) == 3 and 2 in card_counts.values():
            score = 3
        elif 2 in card_counts.values():
            score = 2

        if 'J' in card_counts:
            if card_counts['J'] == 5 or card_counts['J'] == 4:
                score = 7
            elif card_counts['J'] == 3 and len(card_counts) == 2:
                score = 7
            elif card_counts['J'] == 3:
                score = 6
            elif card_counts['J'] == 2 and len(card_counts) == 2:
                score = 7
            elif card_counts['J'] == 2 and len(card_counts) == 3:
                score = 6
            elif card_counts['J'] == 2:
                score = 4
            elif card_counts['J'] == 1 and len(card_counts) == 2:
                score = 7
            elif card_counts['J'] == 1 and len(card_counts) == 3:
                score = 6
            elif card_counts['J'] == 1 and len(card_counts) == 3:
                score = 5
            elif card_counts['J'] == 1 and len(card_counts) == 4:
                score = 4
            elif card_counts['J'] == 1:
                score = 3

        return score

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
            print(card)
            self.winnings += card['bet'] * (i + 1)


solution = Solution('./input_day7.txt')
print(solution.winnings)

# 252973756 wrong (too high)
# 252590412 wrong
