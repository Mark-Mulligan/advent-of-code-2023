class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cube_counts = {"red": 12, "green": 13, "blue": 14}
        self.valid_games = []
        self.valid_ids_total = 0
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                formatted_line = line.strip()
                game_id = int(formatted_line.split(":")[0].split(" ")[1])
                games = formatted_line.split(":")[1].strip().split(";")
                valid_game = True

                for game in games:
                    valid_game = self.is_valid_game(game, game_id)
                    if not valid_game:
                        break

                if valid_game:
                    self.valid_games.append(game_id)
                    self.valid_ids_total += game_id

    def is_valid_game(self, game, game_id):
        draws = [game.strip() for game in game.split(",")]

        for draw in draws:
            [amount, color] = draw.split(" ")

            if int(amount) > self.cube_counts[color]:
                return False

        return True


solution = Solution("./input.txt")
print(solution.valid_ids_total)
print(solution.valid_games)
