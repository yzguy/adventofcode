#
#
#

from util import parse_entries

def part_two_solution(entries):
    es = parse_entries(entries)

    valid_passwords = 0
    for e in es:
        f = e['limit']['lower'] - 1
        s = e['limit']['upper'] - 1
        password = e['password']

        if ((password[f] == e['letter']) ^
        (password[s] == e['letter'])):
            valid_passwords += 1

    return valid_passwords

