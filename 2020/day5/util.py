#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    return lines

def parse_boarding_passes(passes):
    parsed_passes = []
    for boarding_pass in passes:
        row = decode(128, boarding_pass[:7], 'F', 'B')
        column = decode(8, boarding_pass[-3:], 'L', 'R')
        parsed_passes.append({
            boarding_pass: {
                'row': row,
                'column': column,
                'seat': ((row * 8) + column)
            }
        })

    return parsed_passes

def half(numbers):
    return int(((len(numbers) / 2)))

def decode(max_number, letters, lower, upper):
    numbers = list(range(max_number))
    for letter in letters:
        h = half(numbers)
        numbers = {
            lower: numbers[:h],
            upper: numbers[h:]
        }[letter]

    number = numbers[0]

    return number 
