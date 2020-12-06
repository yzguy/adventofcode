#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    return lines

def parse_groups(lines):
    # Append blank line to signal end of group
    lines.append('')

    groups = []
    group = []
    for line in lines:
        if line == '':
            groups.append(list(set(group)))
            group = []
            continue
        for letter in line:
            group.append(letter)

    return groups
