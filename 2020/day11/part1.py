#
#
#

from util import parse_floorplan, apply_rules_to_floorplan


def part_one_solution(entries):
    floorplan = parse_floorplan(entries)

    times_looped = 0
    while True:
        previous = str(floorplan)
        floorplan = apply_rules_to_floorplan(floorplan)
        current = str(floorplan)
        times_looped += 1

        if previous == current:
            total_occupied = 0
            for row in floorplan:
                for col in row:
                    if col["status"] == "#":
                        total_occupied += 1

            return total_occupied
