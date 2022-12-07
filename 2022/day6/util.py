#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = list(reader.read().rstrip())

    return entries


def unique(elems):
    for elem in elems:
        if elems.count(elem) > 1:
            return False
    return True


def find_marker(entries):
    start = 4
    for entry in entries:
        if unique(entries[start-4:start:]):
            return start
        start += 1
