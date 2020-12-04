
#
#

from util import parse_passports

def part_one_solution(entries):
    passports = parse_passports(entries)

    valid = 0
    for passport in passports:
        if ((len(passport.keys()) == 7 and 'cid' not in passport) ^
        (len(passport.keys()) == 8)):
            valid +=1

    return valid
