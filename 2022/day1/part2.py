#
#
#

from util import elves


def part_two_solution(entries):
    e = elves(entries)

    return sum(e[:3])
