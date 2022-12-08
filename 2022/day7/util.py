#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    entries = [entry.split(' ') for entry in entries]

    return entries


def add_child_size_to_parent(directories):
    for d, s in directories.items():
        for i, j in directories.items():
            if i.startswith(d) and d != i:
                directories[d] += j
    return directories


def build_directories(entries):
    path = []
    directories = {}
    for entry in entries:
        cwd = '/'.join(path)
        if entry[0] == '$':
            if entry[1] == 'cd':
                if entry[2] == '..':
                    path.pop()
                elif entry[2] != '/':
                    path.append(entry[2])
                else:
                    path.append('')
            elif entry[1] == 'ls':
                directories[cwd] = 0

        elif entry[0] == 'dir':
            p = f'{cwd}/{entry[1]}'
            if p not in directories:
                directories[p] = 0

        elif entry[0][0].isdigit():
            directories[cwd] += int(entry[0])

    directories = add_child_size_to_parent(directories)

    return directories
