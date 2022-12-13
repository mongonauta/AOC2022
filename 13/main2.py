from functools import cmp_to_key

content = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

with open('input.txt') as f:
    content = f.read()


def has_right_order(left_item, right_item):
    if isinstance(left_item, int) and isinstance(right_item, int):
        return 0 if left_item == right_item else left_item - right_item

    if isinstance(left_item, int):
        return has_right_order([left_item], right_item)

    if isinstance(right_item, int):
        return has_right_order(left_item, [right_item])

    for i in range(min([len(left_item), len(right_item)])):
        order = has_right_order(left_item[i], right_item[i])
        if order == 0:
            continue
        return order

    return 0 if len(left_item) == len(right_item) else len(left_item) - len(right_item)


divider_packets = ([[2]], [[6]])
packets = [
    divider_packets[0],
    divider_packets[1]
]
for line in content.splitlines():
    if not line.strip():
        continue

    p = eval(line.strip())
    packets.append(p)

packets.sort(key=cmp_to_key(has_right_order))
print(
    (packets.index(divider_packets[0]) + 1) * (packets.index(divider_packets[1]) + 1)
)
