#
#
#

from part1 import part_one_solution
from part2 import part_two_solution
import unittest, random


class TestSolutions(unittest.TestCase):
    entries = [
        ['1-3', 'a:', 'abcde'],
        ['1-3', 'b:', 'cdefg'],
        ['2-9', 'c:', 'ccccccccc']
    ]

    random.shuffle(entries)

    def test_part_one_solutions(self):
        self.assertEqual(part_one_solution(self.entries), 2)

    def test_part_two_solutions(self):
        self.assertEqual(part_two_solution(self.entries), 1)

if __name__ == '__main__':
    unittest.main()
