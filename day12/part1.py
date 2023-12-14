import itertools
springs = []
sequence = []


def get_base_combination(springs, sequence):
    result = []
    for i, item in enumerate(sequence):
        for _ in range(item):
            result.append('#')
        if i < len(sequence) - 1:
            result.append('.')

    while len(result) < len(springs):
        result.append('.')

    return result


def get_all_combinations(base_combination, sequence):
    result = ["".join(item) for item in list(
        itertools.product(['#', '.'], repeat=len(base_combination)))]
    filtered_results = []
    for item in result:
        spring_counts = {}
        spring_index = 0
        found_group = False
        for char in item:
            if char == '#':
                found_group = True
                if spring_index in spring_counts:
                    spring_counts[spring_index] += 1
                else:
                    spring_counts[spring_index] = 1
            else:
                if found_group:
                    spring_index += 1
                found_group = False

        if len(spring_counts) == len(sequence):
            add_combination = True
            for i, target in enumerate(sequence):
                if spring_counts[i] != target:
                    add_combination = False

            if add_combination:
                filtered_results.append(item)

    return filtered_results


def get_all_valid_combinations(springs, all_combinations):
    valid_combinations = []

    for combination in all_combinations:
        combination_valid = True
        for i, item in enumerate(springs):
            if item in ['#', '.'] and combination[i] != item:
                combination_valid = False
                break

        if combination_valid:
            valid_combinations.append(combination)

    return valid_combinations


with open('./input_day12.txt') as input:
    total = 0
    for line in input:
        print(line)
        springs = list(line.strip().split(' ')[0])
        sequence = [int(item)
                    for item in line.strip().split(' ')[1].split(',')]

        base_combination = get_base_combination(springs, sequence)
        all_combinations = get_all_combinations(base_combination, sequence)
        valid_combinations = get_all_valid_combinations(
            springs, all_combinations)
        total += len(valid_combinations)

    print(total)
