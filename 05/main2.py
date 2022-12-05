content = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def print_matrix(mtx):
    for x in mtx:
        print(x)


with open('input.txt') as f:
    content = f.read()
    first, rest = content.split('\n\n')
    last_line_len = len(first.splitlines()[-1].rstrip())
    matrix = [[] for _ in range((last_line_len + 2) // 4)]
    for line in first.splitlines():
        for i, c in enumerate(line[1::4]):
            if not c.isspace():
                matrix[i].append(c)

    for stack in matrix:
        stack.reverse()

    for instr in rest.splitlines():
        n, f, d = int(instr.split()[1]), int(instr.split()[3]), int(instr.split()[5])

        to_move = matrix[f - 1][-n:]
        del matrix[f - 1][-n:]

        matrix[d - 1].extend(to_move)

    print(''.join(stack[-1] if stack else '' for stack in matrix))
