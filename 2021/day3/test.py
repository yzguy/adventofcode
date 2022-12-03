#!/usr/bin/env python

from part1 import part_one_solution
from part2 import part_two_solution
import unittest

PART_ONE_ANSWER = 198
PART_TWO_ANSWER = 230


class TestSolutions(unittest.TestCase):
    entries = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), PART_ONE_ANSWER)

    def test_part_two_solution(self):
        self.assertEqual(part_two_solution(self.entries), PART_TWO_ANSWER)


if __name__ == "__main__":
    unittest.main()
