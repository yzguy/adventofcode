#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    return entries
