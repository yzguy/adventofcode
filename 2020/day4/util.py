#
#
#

import re

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    return lines

def parse_passports(lines):
    # Append blank line to signal end
    lines.append('')

    passports = []
    passport = {}
    for line in lines:
        # On blank line, submit passport, reset
        if line == '':
            passports.append(passport)
            passport = {}
            continue
        fields = line.split(' ')
        for field in fields:
            pair = field.split(':')
            passport[pair[0]] = pair[1]

    return passports

def determine_field_validity(passports):
    results = {'valid': [], 'invalid': []}
    for passport in passports:
        if ((len(passport.keys()) == 7 and 'cid' not in passport) ^
        (len(passport.keys()) == 8)):
            results['valid'].append(passport)
        else:
            results['invalid'].append(passport)
    
    return results

def determine_value_validity(passports):
    valid_results = determine_field_validity(passports)['valid']

    results = []
    for result in valid_results:
        valid = True
        for key, value in result.items():
            validated = validate(key, value)
            if not validated:
                valid = False
                break

        if valid:
            results.append(result)

    return results

def validate(key, value):
    validation_func = {
        'byr': byr,
        'iyr': iyr,
        'eyr': eyr,
        'hgt': hgt,
        'hcl': hcl,
        'ecl': ecl,
        'pid': pid,
        'cid': cid
    }[key]

    valid = validation_func(value)

    return valid

def is_within_range(value, start, end):
    try:
        value = int(value)
    except ValueError:
        return False

    if value >= start and value <= end:
        return True

    return False

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def byr(value):
    return is_within_range(value, 1920, 2002)

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def iyr(value):
    return is_within_range(value, 2010, 2020)

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def eyr(value):
    return is_within_range(value, 2020, 2030)

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
def hgt(value):
    try:
        rng = {
            'cm': {
                'start': 150,
                'end': 193
            },
            'in': {
                'start': 59,
                'end': 76
            }
        }[value[-2:]]
    except KeyError:
        return False

    return is_within_range(value[:-2], rng['start'], rng['end'])

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def hcl(value):
    regex = re.compile('^#[a-f0-9]{6}$')
    if regex.match(value):
        return True

    return False

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def ecl(value):
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

# pid (Passport ID) - a nine-digit number, including leading zeroes.
def pid(value):
    regex = re.compile('^[0-9]{9}$')
    if regex.match(value):
        return True

    return False

# cid (Country ID) - ignored, missing or not.
def cid(value):
    return True
