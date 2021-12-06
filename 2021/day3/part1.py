#
#
#

from util import calculate_gamma_rate, calculate_epsilon_rate

def part_one_solution(entries):
    g, gamma = calculate_gamma_rate(entries)
    e, _ = calculate_epsilon_rate(gamma)

    return g * e
