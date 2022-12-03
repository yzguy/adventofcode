#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()
    entries = []
    for line in lines:
        parts = line.split(" ")
        entries.append([parts[0], int(parts[1])])

    return entries


def calculate_position(entries, include_aim=False):
    position, depth, aim = 0, 0, 0

    for entry in entries:
        direction = entry[0]
        value = entry[1]

        if direction == "forward":
            position += value
            if include_aim:
                depth += aim * value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value

    if include_aim:
        return position * depth

    return position * aim
