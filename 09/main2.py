content = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

with open('input.txt') as f:
    content = f.read()

rope = [(0, 0)] * 10
positions_visited = {(0, 0)}

for line in content.splitlines():
    for _ in range(int(line.split()[1])):
        rope[0] = (
            rope[0][0] + (line.split()[0] == 'R') - (line.split()[0] == 'L'),
            rope[0][1] + (line.split()[0] == 'D') - (line.split()[0] == 'U')
        )

        for i in range(1, 10):
            hx, hy = rope[i - 1]
            tx, ty = rope[i]

            if max(abs(tx - hx), abs(ty - hy)) == 2:
                tx, ty = (
                    tx + (tx < hx) - (tx > hx),
                    ty + (ty < hy) - (ty > hy)
                )

            rope[i - 1] = (hx, hy)
            rope[i] = (tx, ty)

        positions_visited.add(rope[-1])

print(len(positions_visited))
