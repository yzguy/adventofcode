#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = list(reader.read().rstrip())

    return entries


def unique(elems):
    if len(elems) > len(set(elems)):
        return False
    return True


def find_sequence(entries, size):
    start = size
    for entry in entries:
        if unique(entries[start-size:start:]):
            return start
        start += 1
