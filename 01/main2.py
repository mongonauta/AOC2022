content = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
with open('input.txt') as f:
    data = ''.join(f.readlines())
    print(sum(sorted(
        [
            sum([int(x) for x in block.strip().split('\n')])
            for block in data.split('\n\n')
        ], reverse=True
    )[:3]))
