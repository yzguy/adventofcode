#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()
    entries = []
    for line in lines:
        parts = line.split(' ')
        entries.append([parts[0], int(parts[1])])

    return entries

def calculate_position(entries, include_aim=False):
    position, depth, aim = 0, 0, 0
    x, y, z = 0, 0, 0

    for entry in entries:
        direction = entry[0]
        value = entry[1]

        if direction == 'forward':
            x += value
            if include_aim:
                y += z * value
        elif direction == 'up':
            z -= value
        elif direction == 'down':
            z += value

    return x * y

def calculate_position_with_aim(entries):
    x, y, aim = 0, 0, 0

    for entry in entries:
        direction = entry[0]
        value = entry[1]

        if direction == 'forward':
            x += value
            y += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value

    return x * y
