#
#
#

from util import extend_line

def part_one_solution(entries, right=3, down=1):
    entries = extend_line(entries, right)
    encountered = 0

    row = 0
    column = 0
    while row < len(entries):
        if entries[row][column] == '#':
            encountered += 1
        row += down
        column += right

    return encountered
