import re


class Solution:
    def __init__(self, file_path):
        self.file_path = file_path
        self.races = []
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                formatted_line = re.sub(r"\s+", " ", line)

                if "Time" in formatted_line:
                    times = [
                        int(time)
                        for time in formatted_line.split(":")[1].strip().split(" ")
                    ]

                    for time in times:
                        self.races.append(
                            {"time": time, "distance": 0, "possibilities": 0}
                        )

                if "Distance" in formatted_line:
                    distances = [
                        int(distance)
                        for distance in formatted_line.split(":")[1].strip().split(" ")
                    ]

                    for i, distance in enumerate(distances):
                        self.races[i]["distance"] = distance

    def calc_races_possibilities(self):
        for race_num, race in enumerate(self.races):
            for i in range(1, race["time"], 1):
                race_time = i + race["distance"] / i

                if race_time < race["time"]:
                    self.races[race_num]["possibilities"] += 1
                # print(i)


solution = Solution("./day_6.txt")
solution.calc_races_possibilities()

answer = 1

for race in solution.races:
    if race["possibilities"] > 0:
        answer *= race["possibilities"]

print(answer)
