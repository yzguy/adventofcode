#
#
#

def part_one_solution(entries):
    entries.sort()

    # Add device adapter joltage
    entries.append(entries[-1] + 3)

    # Keep track of diffs of 1 and 3
    differences = {
        1: 0,
        3: 0
    }

    current_joltage_output = 0
    for entry in entries:
        diff = entry - current_joltage_output
        differences[diff] += 1
        current_joltage_output = entry

    return differences[1] * differences[3]
