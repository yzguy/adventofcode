#
#
#

from util import calculate_oxygen_generator_rating, calculate_cotwo_scrubber_rating

def part_two_solution(entries):
    o, _ = calculate_oxygen_generator_rating(entries)
    c, _ = calculate_cotwo_scrubber_rating(entries)
    return o * c
