#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    e = []
    for entry in entries:
        j = []
        for elem in list(entry):
            j.append(int(elem))
        e.append(j)

    return e


def visible_left(row, col, entries):
    for elem in entries[row][col-1::-1]:
        if elem >= entries[row][col]:
            return False
    return True


def visible_right(row, col, entries):
    for elem in entries[row][col+1::1]:
        if elem >= entries[row][col]:
            return False
    return True


def visible_up(row, col, entries):
    return visible_left(col, row, list(zip(*entries)))


def visible_down(row, col, entries):
    return visible_right(col, row, list(zip(*entries)))


def visible_element(row, col, entries):
    directions = []
    if visible_left(row, col, entries):
        directions.append('left')
    if visible_right(row, col, entries):
        directions.append('right')
    if visible_up(row, col, entries):
        directions.append('up')
    if visible_down(row, col, entries):
        directions.append('down')

    return directions


def find_visible_trees(entries):
    visible = 0
    for row, entry in enumerate(entries):
        for col, elem in enumerate(entry):
            # First row or last col always visible
            if row == 0 or col == 0:
                visible += 1
            # Last row or last col always visible
            elif row == (len(entries) - 1) or col == (len(entry) - 1):
                visible += 1
            # Test neither first/last row or first/last col
            elif visible_element(row, col, entries):
                visible += 1

    return visible
