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

visible = set()

for y in range(min_y, max_y + 1):
    current_height = grid[(y, min_x)]
    visible.add((y, min_x))
    for x in range(min_x + 1, max_x + 1):
        current_pos = (y, x)
        if grid[current_pos] > current_height:
            visible.add(current_pos)
            current_height = grid[current_pos]

    current_height = grid[(y, max_x)]
    visible.add((y, max_x))
    for x in range(max_x, -1, -1):
        current_pos = (y, x)
        if grid[current_pos] > current_height:
            visible.add(current_pos)
            current_height = grid[current_pos]

for x in range(min_x, max_x + 1):
    current_height = grid[(min_y, x)]
    visible.add((min_y, x))
    for y in range(min_y + 1, max_y + 1):
        current_pos = (y, x)
        if grid[current_pos] > current_height:
            visible.add(current_pos)
            current_height = grid[current_pos]

    current_height = grid[(max_y, x)]
    visible.add((max_y, x))
    for y in range(max_y, -1, -1):
        current_pos = (y, x)
        if grid[current_pos] > current_height:
            visible.add(current_pos)
            current_height = grid[current_pos]

print(len(visible))
