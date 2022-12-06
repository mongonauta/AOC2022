examples = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)
]

with open('input.txt') as f:
    examples.append((f.read().strip(), 0))
for e in examples:
    chunks = [e[0][i:i+4] for i in range(len(e[0])) if i + 4 <= len(e[0])]
    for index in range(len(chunks)):
        if len(list(set(chunks[index]))) == 4:
            # assert(index + 4 == e[1])
            print(index + 4)
            break
