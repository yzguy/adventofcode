#!/usr/bin/env python

from part1 import part_one_solution
from part2 import part_two_solution
import unittest

class TestSolutions(unittest.TestCase):
    entries = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
    ]

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), 7)

    def test_part_two_solution(self):
        self.assertEqual(part_two_solution(self.entries), 5)

if __name__ == '__main__':
    unittest.main()
