#
#
#

from util import derange_entries


def part_one_solution(entries):
    entries = derange_entries(entries)

    return entries["count"]
