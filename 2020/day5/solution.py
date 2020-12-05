#!/usr/bin/env python

from util import read_file_to_list
from part1 import part_one_solution
from part2 import part_two_solution


if __name__ == '__main__':
    inputs = read_file_to_list('input.txt')

    part_one_answer = part_one_solution(inputs)
    print(f"Part 1: {part_one_answer}")

    part_two_answer = part_two_solution(inputs)
    print(f'Part 2: {part_two_answer}')
