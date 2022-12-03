#!/usr/bin/env python

from part1 import part_one_solution
from part2 import part_two_solution
import unittest
import random


class TestSolutions(unittest.TestCase):
    entries = [1721, 979, 366, 299, 675, 1456]

    random.shuffle(entries)

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), 514579)

    def test_part_two_solution(self):
        self.assertEqual(part_two_solution(self.entries), 241861950)


if __name__ == "__main__":
    unittest.main()
