#
#
#
from util import find_visible_trees


def part_two_solution(entries):
    _, top_tree = find_visible_trees(entries)
    return top_tree['score']
