#
#
#

from part1 import part_one_solution


def part_two_solution(entries, tests=[]):
    answer = 1
    for test in tests:
        num = part_one_solution(entries, test["right"], test["down"])
        answer *= num

    return answer
