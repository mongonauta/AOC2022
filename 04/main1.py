content = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

with open('input.txt') as f:
    result = 0
    for line in f.readlines():
    # for line in content.strip().split('\n'):
        pairs = line.strip().split(',')

        a_idx = [int(x) for x in pairs[0].split('-')]
        b_idx = [int(x) for x in pairs[1].split('-')]
        result += 1 if (a_idx[0] <= b_idx[0] and a_idx[1] >= b_idx[1]) or (b_idx[0] <= a_idx[0] and b_idx[1] >= a_idx[1]) else 0

    print(result)
