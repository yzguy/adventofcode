#
#
#

from part1 import part_one_solution
from part2 import part_two_solution
import unittest


class TestSolutions(unittest.TestCase):
    entries = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]

    def test_part_one_solutions(self):
        self.assertEqual(part_one_solution(self.entries), 220)

    def test_part_two_solutions(self):
        self.assertEqual(part_two_solution(self.entries), 0)


if __name__ == "__main__":
    unittest.main()
