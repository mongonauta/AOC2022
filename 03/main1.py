import string

content = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

priorities = string.ascii_lowercase[:26] + string.ascii_uppercase[:26]

with open('input.txt') as f:
    result = 0
    for line in f.readlines():
    # for line in content.strip().split('\n'):
        middle_pos = int(len(line.strip()) / 2)
        first_r, right_r = line.strip()[:middle_pos], line.strip()[middle_pos:]
        common = list(set([x for x in first_r if x in right_r]))
        result += priorities.index(common.pop()) + 1

    print(result)
