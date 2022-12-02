content = """
A Y
B X
C Z
"""

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

hands_winners = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}
hands_equal = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

with open('input.txt') as f:
    result = 0
    for line in f.readlines():
    # for line in content.strip().split('\n'):
        hand = line.strip().split()
        print(
            hand,
            list(hands_winners.keys()).index(hand[1]) + 1,
            3 if hands_equal[hand[1]] == hand[0] else 6 if hands_winners[hand[1]] == hand[0] else 0
        )
        result += (
            (list(hands_winners.keys()).index(hand[1]) + 1) +
            (3 if hands_equal[hand[1]] == hand[0] else 6 if hands_winners[hand[1]] == hand[0] else 0)
        )

    print(result)
