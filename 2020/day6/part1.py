#
#
#

from util import parse_groups

def part_one_solution(entries):
    groups = parse_groups(entries)
    sum_of_groups = 0
    for group in groups:
        sum_of_groups += len(group['letters'].keys())

    return sum_of_groups
