#
#
#

from util import make_rucksacks

def part_one_solution(entries):
    rucksacks = make_rucksacks(entries)

    return rucksacks['total']
