#
#

from util import parse_boarding_passes


def part_one_solution(entries):
    boarding_passes = parse_boarding_passes(entries)
    highest_seat_id = boarding_passes["seat_ids"][-1]
    return highest_seat_id
