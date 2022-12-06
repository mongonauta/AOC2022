examples = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)
]

with open('input.txt') as f:
    examples.append((f.read().strip(), 0))


for e in examples:
    chunks = [e[0][i:i+14] for i in range(len(e[0])) if i + 14 <= len(e[0])]
    for index in range(len(chunks)):
        if len(list(set(chunks[index]))) == 14:
            # assert(index + 4 == e[1])
            print(index + 14, e[1])
            break
