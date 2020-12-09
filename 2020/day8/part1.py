#
#
#

from util import parse_instructions, execute_instructions

def part_one_solution(entries):
    instructions = parse_instructions(entries)
    acc, executed = execute_instructions(instructions)

    return acc
