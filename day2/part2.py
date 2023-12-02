class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cube_counts = {"red": 12, "green": 13, "blue": 14}
        self.cube_powers = []
        self.total_power = 0
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                formatted_line = line.strip()
                games = formatted_line.split(":")[1].strip().split(";")
                cube_power = self.get_cube_amounts(games)
                self.cube_powers.append(cube_power)
                self.total_power += cube_power

    def get_cube_amounts(self, games):
        max_amounts = {"red": 0, "green": 0, "blue": 0}

        for game in games:
            draws = [game.strip() for game in game.split(",")]

            for draw in draws:
                [amount, color] = draw.split(" ")

                if int(amount) > max_amounts[color]:
                    max_amounts[color] = int(amount)

        power = 1
        for color in max_amounts:
            power *= max_amounts[color]

        return power


solution = Solution("./input.txt")
print(solution.total_power)
