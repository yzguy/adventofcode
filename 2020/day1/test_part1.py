#!/usr/bin/env python

from part1 import fix_expense_report
import unittest, random

class TestExpenseReport(unittest.TestCase):
    entries = [
        1721,
        979,
        366,
        299,
        675,
        1456
    ]
    
    random.shuffle(entries)

    def test_fix_expense_report(self):
        self.assertEqual(fix_expense_report(self.entries), 514579)

    def test_fix_expense_report_long(self):
        self.assertEqual(fix_expense_report(self.entries), 514579)

if __name__ == '__main__':
    unittest.main()
