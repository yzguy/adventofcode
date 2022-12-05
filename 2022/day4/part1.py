#
#
#

from util import derange_entries


def part_one_solution(entries):
    entries = derange_entries(entries)

    overlaps = [entry['overlap'] for entry in entries if entry['overlap']]

    return len(overlaps)
