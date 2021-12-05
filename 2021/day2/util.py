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

def calculate_position(entries):
    x, y = 0, 0

    for entry in entries:
        direction = entry[0]
        value = entry[1]

        if direction == 'forward':
            x += value
        elif direction == 'up':
            y -= value
        elif direction == 'down':
            y += value

    return x * y
