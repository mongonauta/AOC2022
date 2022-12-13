content = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

# grid = content.split()
with open('input.txt') as f:
    grid = f.read().split()

origin = None
destination = None

for index, line in enumerate(grid):
    if "E" in line:
        destination = (index, line.index("E"))
    if "S" in line:
        origin = (index, line.index("S"))

done = False
buffer = [destination]
grid[destination[0]] = grid[destination[0]].replace("E", "z")
grid[origin[0]] = grid[origin[0]].replace("S", "a")

visited = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
visited[destination[0]][destination[1]] = 0

for posx, posy in buffer:
    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_x = posx + x
        next_y = posy + y

        if any([next_x < 0, next_y < 0, next_x == len(grid), next_y == len(grid[0])]):
            continue

        if ord(grid[posx][posy]) - ord(grid[next_x][next_y]) > 1:
            continue

        # replace if clause for part 2
        # if (next_x, next_y) == origin:
        if grid[next_x][next_y] == "a":
            done = True
            print(visited[posx][posy] + 1)
            break

        if visited[next_x][next_y] is not None:
            continue

        buffer.append((next_x, next_y))
        visited[next_x][next_y] = visited[posx][posy] + 1

    if done:
        break

