
#
#

from util import parse_boarding_passes

def part_one_solution(entries):
    boarding_passes = parse_boarding_passes(entries)

    highest_seat_id = 0
    for boarding_pass in boarding_passes:
        for bid, details in boarding_pass.items():
            if details['seat'] > highest_seat_id:
                highest_seat_id = details['seat']

    return highest_seat_id
