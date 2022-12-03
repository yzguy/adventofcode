#
#
#

from util import play


def part_one_solution(entries):
    rounds = [play(*entry) for entry in entries]

    return sum(rounds)
