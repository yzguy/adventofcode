#!/usr/bin/env python

from part1 import part_one_solution
from part2 import part_two_solution
from util import read_file_to_list, derange
import unittest

PART_ONE_ANSWER = 2
PART_TWO_ANSWER = 4


class TestSolutions(unittest.TestCase):
    entries = read_file_to_list("test_input.txt")

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), PART_ONE_ANSWER)

    def test_part_two_solution(self):
        self.assertEqual(part_two_solution(self.entries), PART_TWO_ANSWER)

class TestUtil(unittest.TestCase):

    def test_derange(self):
        cases = [
            "13-16",
            "20-25",
            "3-4",
        ]

        results = [
            list(range(13, 17)),
            list(range(20, 26)),
            list(range(3, 5)),
        ]

        for idx, case in enumerate(cases):
            self.assertEqual(results[idx], derange(case))

if __name__ == "__main__":
    unittest.main()
