from pprint import pprint


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.seeds = []
        self.maps = {}
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            current_map = ""

            for line in input:
                formatted_line = line.strip()

                if "seeds" in formatted_line:
                    seed_positions = [
                        int(seed)
                        for seed in formatted_line.split(":")[1].strip().split(" ")
                    ]

                    for i, seed in enumerate(seed_positions):
                        if i % 2 == 0:
                            min_seed = seed
                            max_seed = seed + seed_positions[i + 1]
                            self.seeds.append(min_seed, max_seed)

                if "map" in formatted_line:
                    current_map = formatted_line.split(" ")[0].strip()
                    continue

                if not formatted_line:
                    current_map = ""
                    continue

                if current_map:
                    if current_map not in self.maps:
                        self.maps[current_map] = {}

                    [end, start, map_range] = [
                        int(num) for num in formatted_line.split(" ")
                    ]

                    for i in range(start, start + map_range, 1):
                        print(i)
                        count_index = i - start
                        self.maps[current_map][i] = end + count_index

    def map_seeds(self, map_to_use):
        new_seed_values = []

        for seed in self.seeds:
            if seed in self.maps[map_to_use]:
                new_seed_values.append(self.maps[map_to_use][seed])
            else:
                new_seed_values.append(seed)

        self.seeds = new_seed_values

    def get_min_seed_location(self):
        return min(self.seeds)


solution = Solution("./input_day5.txt")
print(solution.seeds)
for map in solution.maps:
    solution.map_seeds(map)

print(solution.seeds)
print(solution.get_min_seed_location())
