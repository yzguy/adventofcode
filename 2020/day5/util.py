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
        row = get_number(boarding_pass[:7], 'F', 'B')
        column = get_number(boarding_pass[-3:], 'L', 'R')
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

# Each part can be converted to binary to get decimal number
# Replace Lower/Upper letter with 0 or 1 respectively
# Convert to base 2 integer
def get_number(letters, lower, upper):
    return int(letters.replace(lower, '0').replace(upper, '1'), 2)

# Below functions do the process outlined in prompt
# Take lower/upper half of list based on letter
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
