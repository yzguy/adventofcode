#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    return lines

def parse_instructions(instructions):
    parsed_instructions = []

    for instruction in instructions:
        instruction = instruction.split(' ')
        operation = instruction[0]
        argument = int(instruction[1].replace('+', ''))

        parsed_instructions.append({
            'operation': operation,
            'argument': argument,
            'executed': False
        })

    return parsed_instructions

def execute_instructions(instructions):
    index, acc, executed = 0, 0, False
    while True:
        # If index out of range
        # program successfully ran
        # break to terminate
        try:
            instruction = instructions[index]
        except IndexError:
            break
        operation = instruction['operation']
        argument = instruction['argument']

        if instruction['executed']:
            executed = True
            break

        if operation == 'acc':
            acc += argument
            index += 1
        elif operation == 'jmp':
            index += argument
        elif operation == 'nop':
            index += 1

        instruction['executed'] = True
    return acc, executed
