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


result = 0
for index, value in enumerate(content.split('\n\n'), start=1):
    left, right = eval(value.splitlines()[0]), eval(value.splitlines()[1])
    if has_right_order(left, right) < 0:
        result += index

print(result)
