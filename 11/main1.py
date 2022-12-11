# monkeys = [
#     {
#         'items': [79, 98],
#         'test': 23,
#         'target': [2, 3],
#         'operation': {
#             'variant': 'mul',
#             'value': 19
#         },
#         'inspects': 0
#     },
#     {
#         'items': [54, 65, 75, 74],
#         'test': 19,
#         'target': [2, 0],
#         'operation': {
#             'variant': 'sum',
#             'value': 6
#         },
#         'inspects': 0
#     },
#     {
#         'items': [79, 60, 97],
#         'test': 13,
#         'target': [1, 3],
#         'operation': {
#             'variant': 'mul',
#             'value': None
#         },
#         'inspects': 0
#     },
#     {
#         'items': [74],
#         'test': 17,
#         'target': [0, 1],
#         'operation': {
#             'variant': 'sum',
#             'value': 3
#         },
#         'inspects': 0
#     }
# ]

monkeys = [
    {
        'items': [97, 81, 57, 57, 91, 61],
        'test': 11,
        'target': [5, 6],
        'operation': {
            'variant': 'mul',
            'value': 7
        },
        'inspects': 0
    },
    {
        'items': [88, 62, 68, 90],
        'test': 19,
        'target': [4, 2],
        'operation': {
            'variant': 'mul',
            'value': 17
        },
        'inspects': 0
    },
    {
        'items': [74, 87],
        'operation': {
            'variant': 'sum',
            'value': 2
        },
        'test': 5,
        'target': [7, 4],
        'inspects': 0
    },
    {
        'items': [53, 81, 60, 87, 90, 99, 75],
        'operation': {
            'variant': 'sum',
            'value': 1
        },
        'test': 2,
        'target': [2, 1],
        'inspects': 0
    },
    {
        'items': [57],
        'operation': {
            'variant': 'sum',
            'value': 6
        },
        'test': 13,
        'target': [7, 0],
        'inspects': 0
    },
    {
        'items': [54, 84, 91, 55, 59, 72, 75, 70],
        'operation': {
            'variant': 'mul',
            'value': None
        },
        'test': 7,
        'target': [6, 3],
        'inspects': 0
    },
    {
        'items': [95, 79, 79, 68, 78],
        'operation': {
            'variant': 'sum',
            'value': 3
        },
        'test': 3,
        'target': [1, 3],
        'inspects': 0
    },
    {
        'items': [61, 97, 67],
        'operation': {
            'variant': 'sum',
            'value': 4
        },
        'test': 17,
        'target': [0, 5],
        'inspects': 0
    }
]

for _ in range(20):
    print('-----------------------')
    for m in monkeys:
        for index, item in enumerate(m['items']):
            variation = m['operation']['value'] if m['operation']['value'] else item
            worry_level = int((item * variation if m['operation']['variant'] == 'mul' else item + variation) / 3)
            target = m['target'][0] if worry_level % m['test'] == 0 else m['target'][1]
            monkeys[target]['items'].append(worry_level)
            m['inspects'] += 1

        m['items'] = []

    for index, m in enumerate(monkeys):
        print('Monkey {index}: {items}'.format(index=index, items=','.join([str(x) for x in m['items']])))

    print('')

for index, m in enumerate(monkeys):
    print('Monkey {index} inspected items {times}'.format(index=index, times=m['inspects']))

results = sorted([x['inspects'] for x in monkeys], reverse=True)
print('Inspects: {} -> {}'.format(results, results[0] * results[1]))
