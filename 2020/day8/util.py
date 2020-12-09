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
