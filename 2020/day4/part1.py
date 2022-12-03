#
#

from util import parse_passports, determine_field_validity


def part_one_solution(entries):
    passports = parse_passports(entries)
    results = determine_field_validity(passports)
    valid = len(results["valid"])
    return valid
