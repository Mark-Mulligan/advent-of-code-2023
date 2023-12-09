from pprint import pprint


class Solution():
    def __init__(self, file_path):
        self.file_path = file_path
        self.num_patterns = []
        self.read_input()

    def read_input(self):
        with open(self.file_path) as input:
            for line in input:
                nums = [int(num) for num in line.strip().split(' ')]
                self.num_patterns.append(nums)

    def make_branch(self, nums):
        return [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

    def make_tree(self, num_pattern):
        tree = [num_pattern]
        current_pattern = num_pattern

        while all(element == 0 for element in current_pattern) is False:
            new_branch = self.make_branch(current_pattern)
            tree.append(new_branch)
            current_pattern = new_branch

        return tree

    def add_new_values(self, tree):
        current_branch_index = len(tree) - 1
        tree[current_branch_index].append(0)

        while current_branch_index > 0:
            new_num = tree[current_branch_index][-1] + \
                tree[current_branch_index - 1][-1]
            tree[current_branch_index - 1].append(new_num)
            current_branch_index -= 1

        return tree

    def create_new_trees(self):
        new_trees = []

        for nums in self.num_patterns:
            tree = self.make_tree(nums)
            new_tree = self.add_new_values(tree)
            new_trees.append(new_tree)

        return new_trees

    def get_answer(self):
        new_trees = self.create_new_trees()
        total = 0

        for tree in new_trees:
            total += tree[0][-1]

        return total


solution = Solution('./input_day9.txt')
answer = solution.get_answer()
pprint(answer)
