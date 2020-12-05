#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    return lines

def parse_boarding_passes(boarding_passes):
    parsed_passes = { 'boarding_passes': [], 'seat_ids': [] }
    for boarding_pass in boarding_passes:
        row = decode(128, boarding_pass[:7], 'F', 'B')
        column = decode(8, boarding_pass[-3:], 'L', 'R')
        seat = ((row * 8) + column)
        parsed_passes['seat_ids'].append(seat)
        parsed_passes['boarding_passes'].append({
            boarding_pass: {
                'row': row,
                'column': column,
                'seat': seat
            }
        })

        parsed_passes['seat_ids'].sort()

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
