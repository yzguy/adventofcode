#
#
#

from util import make_groups


def part_two_solution(entries):
    groups = make_groups(entries)

    return groups["total"]
