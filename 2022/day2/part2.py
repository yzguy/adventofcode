#
#
#

from util import play, strategy_guide


def part_two_solution(entries):
    rounds = [play(*entry) for entry in strategy_guide(entries)]

    return sum(rounds)
