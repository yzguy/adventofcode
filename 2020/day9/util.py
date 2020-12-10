#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    lines = [int(line) for line in lines]

    return lines

def find_numbers_for_sum(numbers, total):
    for num in numbers:
        difference = total - num
        if difference in numbers:
            return {
                'numbers': [num, difference],
                'total': total
            }

    return {}
