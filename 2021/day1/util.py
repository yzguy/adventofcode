#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()
    entries = [int(entry) for entry in entries]

    return entries

def find_increases(entries):
    increases = 0

    for idx, entry in enumerate(entries):
        if entry > entries[idx-1]:
            increases += 1

    return increases

def find_sliding_window_increases(entries):
    totals = []
    for idx, entry in enumerate(entries):
        window = entries[idx:idx+3]

        if len(window) < 3:
            break

        totals.append(sum(window))

    increases = find_increases(totals)
    return increases
