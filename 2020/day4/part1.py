
#
#

from util import parse_passports, determine_validity

def part_one_solution(entries):
    passports = parse_passports(entries)
    valid = determine_validity(passports)
    return valid
