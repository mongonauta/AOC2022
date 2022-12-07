content = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

with open('input.txt') as f:
    content = f.read()

directories = {
    '/': {
        'size': 0
    }
}

current_dir = ['/']

for line in content.strip().split('\n'):
    line_output = line.strip().split()
    if line_output[0] == '$':
        if line_output[1] == 'cd':
            if line_output[2] == '/':
                current_dir = ['/']

            elif line_output[2] == '..':
                current_dir = current_dir[:-1]

            else:
                current_dir.append(line_output[2])
    elif line_output[0] == 'dir':
        key = '_'.join(current_dir + [line_output[1]])
        if key not in directories:
            directories[key] = {
                'size': 0
            }
    else:
        current_path = []
        for x in current_dir:
            current_path.append(x)
            key = '_'.join(current_path)
            directories[key]['size'] += int(line_output[0])

unused_space = 70000000 - directories['/']['size']
required_space = 30000000 - unused_space
print(min([value['size'] for key, value in directories.items() if value['size'] >= required_space]))
