#!/usr/bin/env python

from util import read_file_to_list

# Most efficient solution
def fix_expense_report(entries):
    for entry in entries:
        difference = 2020 - entry
        if difference in entries:
            return difference * entry

# My initial solution
def fix_expense_report_long(entries):
    for i, e in enumerate(entries):
        es = entries.copy()
        del es[i]
        for re in es:
            if e + re == 2020:
                return e * re

if __name__ == '__main__':
    entries = read_file_to_list('input.txt')
    answer = fix_expense_report(entries)
    print(answer)
