#
#
#

def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()
    return entries

def calculate_gamma_rate(entries):
    gamma = ''
    for i in range(len(entries[0])):
        zeroes, ones = 0, 0
        for row in entries:
            if row[i] == '0':
                zeroes += 1
            elif row[i] == '1':
                ones += 1

        if zeroes > ones:
            gamma += '0'
        else:
            gamma += '1'

    decimal = int(gamma, 2)

    return decimal, gamma

def calculate_epsilon_rate(gamma):
    epsilon = ''
    for bit in gamma:
        if bit == '0':
            epsilon += '1'
        elif bit == '1':
            epsilon += '0'

    decimal = int(epsilon, 2) 

    return decimal, epsilon
