#
#
#

from util import parse_instructions

def part_one_solution(entries):
    instructions = parse_instructions(entries)

    index, acc = 0, 0
    while True:
        instruction = instructions[index]
        operation = instruction['operation']
        argument = instruction['argument']

        if instruction['executed']:
            break

        if operation == 'nop':
            index += 1
        elif operation == 'acc':
            acc += argument
            index += 1
        elif operation == 'jmp':
            index += argument

        instruction['executed'] = True

    return acc
