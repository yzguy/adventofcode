#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    lines = [int(line) for line in lines]

    return lines
