#
#
#


from util import parse_instructions, execute_instructions
import copy

def part_two_solution(entries):
    instructions = parse_instructions(entries)

    for index in range(len(instructions)):
        test_copy = copy.deepcopy(instructions)
        operation = instructions[index]['operation']
        if operation in ['jmp', 'nop']:
            if operation == 'jmp':
                test_copy[index]['operation'] = 'nop'
            elif operation == 'nop':
                test_copy[index]['operation'] = 'jmp'

            acc, executed = execute_instructions(test_copy)
            if not executed:
                return acc
