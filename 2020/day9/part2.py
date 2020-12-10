#
#
#

from part1 import part_one_solution

def part_two_solution(entries, preamble_size=25):
    solution = part_one_solution(entries, preamble_size)

    start = 0
    end = len(entries)

    for index, num in enumerate(entries):
        total = [num]

        for element in entries[index + 1:]:
            total.append(element)
            total.sort()
            if sum(total) == solution:
                return total[0] + total[-1]
