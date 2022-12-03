#
#

from util import parse_rules, find_rules_containing_bag


def part_one_solution(entries):
    rules = parse_rules(entries)

    my_bag = "shiny gold"

    containing_rules = find_rules_containing_bag(my_bag, rules)
    for rule in containing_rules:
        containing_rules.extend(find_rules_containing_bag(rule["name"], rules))

    names = set([rule["name"] for rule in containing_rules])
    total = len(names)

    return total
