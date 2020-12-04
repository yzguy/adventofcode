#
#
#

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

