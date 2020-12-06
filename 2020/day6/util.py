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

    groups, group, count = [], {'letters': {}, 'size': 0}, 0
    for line in lines:
        count += 1
        if line == '':
            group['size'] = count - 1
            groups.append(group)
            group, count = {'letters': {}, 'size': 0}, 0
            continue
        for letter in line:
            if letter in group['letters']:
                group['letters'][letter] += 1
            else:
                group['letters'][letter] = 1

    return groups
