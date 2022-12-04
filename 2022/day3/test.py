#!/usr/bin/env python

from part1 import part_one_solution
from part2 import part_two_solution
from util import read_file_to_list, split_entry, shared_item, letter_to_priority
import unittest

PART_ONE_ANSWER = 157
PART_TWO_ANSWER = 70


class TestSolutions(unittest.TestCase):
    entries = read_file_to_list("test_input.txt")

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), PART_ONE_ANSWER)

    def test_part_two_solution(self):
        self.assertEqual(part_two_solution(self.entries), PART_TWO_ANSWER)

class TestUtil(unittest.TestCase):

    def test_split_entry(self):
        cases = [
            'abc123',
            '111222',
            '808aaa',
        ]

        results = [
            # first, second
            ('abc', '123'),
            ('111', '222'),
            ('808', 'aaa'),
        ]

        for idx, case in enumerate(cases):
            self.assertEqual(results[idx], split_entry(case))

    def test_shared_item(self):
        cases = [
            [['A', 'B', 'C'], ['C', 'D', 'E']],
            [['Z', 'L', 'M'], ['M', 'N', 'E'], ['F', 'M', 'Q']],
        ]

        results = [
            'C',
            'M',
        ]

        for idx, case in enumerate(cases):
            self.assertEqual(results[idx], shared_item(*case))

    def test_letter_to_priority(self):
        cases = ['A', 'x', 'O']
        results = [27, 24, 41]

        for idx, case in enumerate(cases):
            self.assertEqual(results[idx], letter_to_priority(case))

if __name__ == "__main__":
    unittest.main()
