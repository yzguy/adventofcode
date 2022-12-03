#
#
#

from util import parse_entries


def part_one_solution(entries):
    es = parse_entries(entries)

    valid_passwords = 0
    for e in es:
        count = e["password"].count(e["letter"])
        if count >= e["limit"]["lower"] and count <= e["limit"]["upper"]:
            valid_passwords += 1

    return valid_passwords
