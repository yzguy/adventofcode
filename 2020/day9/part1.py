#
#
#

from util import find_numbers_for_sum


def part_one_solution(entries, preamble_size=25):
    current = preamble_size

    for entry in entries[current:]:
        start, end = (current - preamble_size), current
        preamble = entries[start:end]

        solution = find_numbers_for_sum(preamble, entry)
        if not solution:
            return entry

        current += 1
