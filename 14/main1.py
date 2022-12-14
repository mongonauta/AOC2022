content = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

with open('input.txt') as f:
    content = f.read()


def generate_rocks(data):
    current_max_y = 0

    rocks_read = set()
    for paths in data.splitlines():
        p = paths.split(' -> ')
        for i in range(len(p) - 1):
            x, y = int(p[i].split(",")[0]), int(p[i].split(",")[1])
            xx, yy = int(p[i + 1].split(",")[0]), int(p[i + 1].split(",")[1])

            sx = 1 if x <= xx else -1
            sy = 1 if y <= yy else -1

            for x in range(x, xx + sx, sx):
                for y in range(y, yy + sy, sy):
                    rocks_read.add((x, y))

                current_max_y = y if y > current_max_y else current_max_y

    return rocks_read, current_max_y


def run(rocks, sand, source_x, source_y, current_max_y, is_source=True):
    while True:
        if (source_x, source_y) in sand:
            break

        x = source_x
        y = source_y
        while (x, y + 1) not in rocks and (x, y + 1) not in sand:
            y += 1
            if y > current_max_y:
                return sand, True

        if (x - 1, y + 1) not in rocks and (x - 1, y + 1) not in sand:
            sand, is_end = run(rocks, sand, x - 1, y + 1, current_max_y, False)
            if is_end:
                break

        elif (x + 1, y + 1) not in rocks and not (x + 1, y + 1) in sand:
            sand, is_end = run(rocks, sand, x + 1, y + 1, current_max_y, False)
            if is_end:
                break

        else:
            sand.add((x, y))
            if not is_source:
                return sand, False

    return sand, True


total_rocks, max_y = generate_rocks(content)

sand_source = (500, 0)
result, _ = run(total_rocks, set(), sand_source[0], sand_source[1], max_y)
print(len(result))
