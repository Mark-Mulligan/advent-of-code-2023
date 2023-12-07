import re


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.races = []
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                formatted_line = re.sub(r"\s+", "", line)

                if "Time" in formatted_line:
                    time = formatted_line.split(":")[1]

                    self.races.append(
                        {"time": int(time), "distance": 0, "possibilities": 0}
                    )

                if "Distance" in formatted_line:
                    distance = formatted_line.split(":")[1]
                    self.races[0]["distance"] = int(distance)

    def calc_races_possibilities(self):
        for race_num, race in enumerate(self.races):
            for i in range(1, race["time"], 1):
                race_time = i + race["distance"] / i

                if race_time < race["time"]:
                    self.races[race_num]["possibilities"] += 1


solution = Solution("./day_6.txt")
solution.calc_races_possibilities()

answer = 1

for race in solution.races:
    if race["possibilities"] > 0:
        answer *= race["possibilities"]

print(answer)
