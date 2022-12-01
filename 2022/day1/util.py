#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()
    # Add blank as a stop after last elf
    entries.append("")

    return entries


def elves(entries):
    elves = []

    elf = 0
    for entry in entries:
        if entry == "":
            elves.append(elf)
            elf = 0
            continue
        elf += int(entry)
    elves = sorted(elves, reverse=True)

    return elves
