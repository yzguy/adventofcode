#
#
#

def part_one_solution(entries):
    encountered = 0

    column = 0
    for row, _ in enumerate(entries):
        if entries[row][column] == '#':
            encountered += 1
        column += 3

    return encountered
