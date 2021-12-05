#!/usr/bin/env python

from part1 import part_one_solution
from part2 import part_two_solution
import unittest

PART_ONE_ANSWER = None
PART_TWO_ANSWER = None

class TestSolutions(unittest.TestCase):
    entries = [
    ]

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), PART_ONE_ANSWER)

    def test_part_two_solution(self):
        self.assertEqual(part_two_solution(self.entries), PART_TWO_ANSWER)

if __name__ == '__main__':
    unittest.main()

