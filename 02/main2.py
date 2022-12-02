content = """
A Y
B X
C Z
"""

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

results = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
hands = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

with open('input.txt') as f:
    result = 0
    for line in f.readlines():
    # for line in content.strip().split('\n'):
        h = line.strip().split()

        hand = None
        l = list(hands.keys())
        if h[1] == 'X':
            hand = hands[h[0]]

        elif h[1] == 'Y':
            hand = h[0]

        elif h[1] == 'Z':
            l.remove(h[0])
            l.remove(hands[h[0]])
            hand = l[0]
        print(
            h,
            hand,
            list(hands.keys()).index(hand) + 1,
            results[h[1]]
        )
        result += (
            (list(hands.keys()).index(hand) + 1) +
            (results[h[1]])
        )

    print(result)
