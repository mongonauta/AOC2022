content = """30373
25512
65332
33549
35390"""

with open('input.txt') as f:
    content = f.read()

grid = {}
for y, line in enumerate(content.splitlines()):
    for x, c in enumerate(line):
        grid[(x, y)] = int(c)

min_y, min_x = min(grid)
max_y, max_x = max(grid)

score = -1

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        tree_height = grid[(y, x)]

        up_score, down_score, right_score, left_score = 0, 0, 0, 0

        for yy in range(y - 1, min_y - 1, -1):
            up_score += 1
            if grid[(yy, x)] >= tree_height:
                break

        for yy in range(y + 1, max_y + 1):
            down_score += 1
            if grid[(yy, x)] >= tree_height:
                break

        for xx in range(x - 1, min_x - 1, -1):
            left_score += 1
            if grid[(y, xx)] >= tree_height:
                break

        for xx in range(x + 1, max_x + 1):
            right_score += 1
            if grid[(y, xx)] >= tree_height:
                break

        score = max(up_score * down_score * right_score * left_score, score)

print(score)
