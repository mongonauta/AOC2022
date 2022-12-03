import collections
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
    lines = f.readlines()
    for group in [[x.strip() for x in lines[i:i + 3]] for i in range(0, len(lines), 3)]:
    # for group in [content.strip().split('\n')[i:i+3] for i in range(0, len(content.strip().split('\n')), 3)]:
        common = list(set([x for x in group[0] if x in group[1] and x in group[2]]))
        result += priorities.index(common.pop()) + 1

    print(result)
