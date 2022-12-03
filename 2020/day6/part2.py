#
#
#

from util import parse_groups


def part_two_solution(entries):
    groups = parse_groups(entries)

    sum_of_groups = 0
    for group in groups:
        all_answered = 0
        for letter, count in group["letters"].items():
            if count == group["size"]:
                all_answered += 1

        sum_of_groups += all_answered

    return sum_of_groups
