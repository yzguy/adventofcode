#
#
#

from util import parse_entries

def part_two_solution(entries):
    es = parse_entries(entries)

    valid_passwords = 0
    for e in es:
        first_position = False
        second_position = False
        f = e['limit']['lower'] - 1
        s = e['limit']['upper'] - 1
        if e['password'][f] == e['letter']:
            first_position = True

        if e['password'][s] == e['letter']:
            second_position = True

        if first_position and not second_position:
            valid_passwords += 1
        elif not first_position and second_position:
            valid_passwords += 1

    return valid_passwords

