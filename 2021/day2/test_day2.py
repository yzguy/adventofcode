#!/usr/bin/env python

from part1 import part_one_solution
#from part2 import part_two_solution
import unittest

class TestSolutions(unittest.TestCase):
    entries = [
        ['forward', 5],
        ['down', 5],
        ['forward', 8],
        ['up', 3],
        ['down', 8],
        ['forward', 2]
    ]

    def test_part_one_solution(self):
        self.assertEqual(part_one_solution(self.entries), 150)

    #def test_part_two_solution(self):
    #    self.assertEqual(part_two_solution(self.entries), 5)

if __name__ == '__main__':
    unittest.main()

