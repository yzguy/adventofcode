#!/usr/bin/env python

from part1 import part_one_solution
from part2 import part_two_solution
from util import read_file_to_list, unique
import unittest

PART_ONE_ANSWER = 7
PART_TWO_ANSWER = 19


class TestSolutions(unittest.TestCase):
    entries = read_file_to_list("test_input.txt")

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), PART_ONE_ANSWER)

    def test_part_two_solution(self):
        self.assertEqual(part_two_solution(self.entries), PART_TWO_ANSWER)


class TestUtil(unittest.TestCase):

    def test_unique(self):
        cases = [
            [1, 1, 2, 3],
            [1, 2, 3, 4],
        ]

        self.assertEqual(False, unique(cases[0]))
        self.assertEqual(True, unique(cases[1]))


if __name__ == "__main__":
    unittest.main()
