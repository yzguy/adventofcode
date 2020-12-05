#!/usr/bin/env python

from util import read_file_to_list
from util import parse_boarding_passes

RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

def draw(entries):
    seating = [list('X' * 8) for row in range(128)] 

    boarding_passes = parse_boarding_passes(entries)
    for boarding_pass in boarding_passes['boarding_passes']:
        for boarding_pass_id, details in boarding_pass.items():
            row = details['row']
            column = details['column']
            seating[row][column] = 'O'

    for row in seating:
        for seat in row:
            if seat == 'X':
                print(f'{GREEN}{seat}{END}', end=' ')
            elif seat == 'O':
                print(f'{RED}{seat}{END}', end=' ')
        print()

if __name__ == '__main__':
    inputs = read_file_to_list('input.txt')
    draw(inputs)
