#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()
    entries = [int(entry) for entry in entries]

    return entries


def find_numbers_for_sum(entries, total=2020):
    for entry in entries:
        difference = total - entry
        if difference in entries:
            return {
                'numbers': [entry, difference],
                'product': entry * difference
            }
