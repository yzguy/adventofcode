#
#
#

from util import parse_rules, how_many_bags_within


def part_two_solution(entries):
    rules = parse_rules(entries)

    my_bag = "shiny gold"
    total = how_many_bags_within(my_bag, rules)

    return total
