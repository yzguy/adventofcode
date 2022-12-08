#
#
#
from util import build_directories

TOTAL_SIZE = 70000000
NEEDED_SPACE = 30000000


def part_two_solution(entries):
    directories = build_directories(entries)
    directories = dict(sorted(directories.items(), key=lambda x: x[1]))

    needed_space = NEEDED_SPACE - (TOTAL_SIZE - directories[''])
    for d, s in directories.items():
        if s >= needed_space:
            return s
