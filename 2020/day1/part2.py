#
#
#

from util import find_numbers_for_sum
import math


def part_two_solution(entries):
    for index, entry in enumerate(entries):
        copy = entries.copy()
        del copy[index]

        solution = find_numbers_for_sum(copy, 2020 - entry)
        if solution is not None:
            return math.prod(solution["numbers"]) * entry
