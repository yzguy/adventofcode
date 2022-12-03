#
#
#

from util import parse_boarding_passes


def part_two_solution(entries):
    boarding_passes = parse_boarding_passes(entries)

    seat_ids = boarding_passes["seat_ids"]
    first, last = seat_ids[0], seat_ids[-1]
    missing = list(set(range(first, last)) - set(seat_ids))[0]

    return missing
