#
#
#
from util import build_directories


def part_one_solution(entries):
    directories = build_directories(entries)
    sum = 0
    for d, s in directories.items():
        if s <= 100000:
            sum += s

    return sum
