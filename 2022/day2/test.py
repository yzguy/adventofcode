#!/usr/bin/env python

from part1 import part_one_solution
from part2 import part_two_solution
from util import read_file_to_list, play, strategy_guide
import unittest

PART_ONE_ANSWER = 15
PART_TWO_ANSWER = 12


class TestSolutions(unittest.TestCase):
    entries = read_file_to_list("test_input.txt")

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), PART_ONE_ANSWER)

    def test_part_two_solution(self):
        self.assertEqual(part_two_solution(self.entries), PART_TWO_ANSWER)

class TestUtil(unittest.TestCase):
    cases = [
        ['A', 'Y'],
        ['B', 'X'],
        ['C', 'Z'],
    ]

    def test_play(self):
        scores = [8, 1, 6]

        for idx, case in enumerate(TestUtil.cases):
            self.assertEqual(scores[idx], play(*case))

    def test_strategy_guide(self):
        entries = [
            ['A', 'X'],
            ['B', 'X'],
            ['C', 'X']
        ]
        self.assertEqual(entries, strategy_guide(TestUtil.cases))

if __name__ == "__main__":
    unittest.main()
