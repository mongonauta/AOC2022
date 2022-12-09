content = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

with open('input.txt') as f:
    content = f.read()

hx, hy, tx, ty = 0, 0, 0, 0

positions_visited = {(tx, ty)}
for line in content.splitlines():
    for _ in range(int(line.split()[1])):
        hx, hy = (
            hx + (line.split()[0] == 'R') - (line.split()[0] == 'L'),
            hy + (line.split()[0] == 'D') - (line.split()[0] == 'U')
        )

        if max(abs(tx - hx), abs(ty - hy)) == 2:
            tx, ty = (
                tx + (tx < hx) - (tx > hx),
                ty + (ty < hy) - (ty > hy)
            )

        positions_visited.add((tx, ty))

print(len(positions_visited))
