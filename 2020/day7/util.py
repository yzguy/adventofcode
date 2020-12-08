#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    return lines

def parse_rules(rules):
    parsed_rules = []

    rules = clean_rules(rules)
    for rule in rules:
        bag, contents = rule[0], rule[1]

        contents = parse_contents(contents)
        parsed_rules.append({
            'name': bag,
            'contents': contents
        })

    return parsed_rules

def clean_rules(rules):
    rs = []
    for rule in rules:
        # Get rid of unnecessary words/characters
        for word in ['bags', 'bag', '.']:
            rule = rule.replace(word, '')

        # Replace no other bags
        rule = rule.replace('no other', '0 other')
        # Split on contain
        rule = rule.split('contain')
        # Strip spaces
        rule = [part.strip() for part in rule]

        rule[1] = rule[1].split(' , ')

        rs.append(rule)

    return rs

def parse_contents(contents):
    parsed_contents = {}
    for element in contents:
        # Return empty dict if it contains nothing
        if element == '0 other':
            break

        element = element.split(' ')
        key = ' '.join(element[1:])

        parsed_contents[key] = int(element[0])

    return parsed_contents

def find_rules_containing_bag(bag, rules):
    inside = []
    for rule in rules:
        if bag in rule['contents'].keys():
            inside.append(rule)

    return inside
