#
#
#

from part1 import part_one_solution
from part2 import part_two_solution
import unittest


class TestSolutions(unittest.TestCase):
    entries = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]

    def test_part_one_solutions(self):
        self.assertEqual(part_one_solution(self.entries, 5), 127)

    def test_part_two_solutions(self):
        self.assertEqual(part_two_solution(self.entries, 5), 62)


if __name__ == "__main__":
    unittest.main()
