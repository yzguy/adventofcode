#
#
#

from util import parse_passports, determine_value_validity


def part_two_solution(entries):
    passports = parse_passports(entries)
    results = determine_value_validity(passports)
    valid = len(results)
    return valid
