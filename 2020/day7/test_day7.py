#
#
#

from part1 import part_one_solution
from part2 import part_two_solution
import unittest


class TestSolutions(unittest.TestCase):
    entries = [
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.'
    ]

    def test_part_one_solutions(self):
        self.assertEqual(part_one_solution(self.entries), 4)

    def test_part_two_solutions(self):
        self.assertEqual(part_two_solution(self.entries), 32)

if __name__ == '__main__':
    unittest.main()
