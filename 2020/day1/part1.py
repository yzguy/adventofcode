#
#
#

from util import find_numbers_for_sum

def part_one_solution(entries):
    numbers = find_numbers_for_sum(entries)
    return numbers['product']
