#
#
#
from util import derange_entries


def part_two_solution(entries):
    entries = derange_entries(entries, any=True)

    return entries["count"]
