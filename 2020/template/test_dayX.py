#
#
#

from part1 import part_one_solution
from part2 import part_two_solution
import unittest


class TestSolutions(unittest.TestCase):
    entries = []

    def test_part_one_solutions(self):
        self.assertEqual(part_one_solution(self.entries), 0)

    def test_part_two_solutions(self):
        self.assertEqual(part_two_solution(self.entries), 0)


if __name__ == "__main__":
    unittest.main()
