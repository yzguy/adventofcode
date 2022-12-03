#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()
    return entries


def calculate_gamma_rate(entries):
    gamma = ""
    for i in range(len(entries[0])):
        zeroes, ones = 0, 0
        for row in entries:
            if row[i] == "0":
                zeroes += 1
            elif row[i] == "1":
                ones += 1

        if zeroes > ones:
            gamma += "0"
        else:
            gamma += "1"

    decimal = int(gamma, 2)

    return decimal, gamma


def calculate_epsilon_rate(gamma):
    epsilon = ""
    for bit in gamma:
        if bit == "0":
            epsilon += "1"
        elif bit == "1":
            epsilon += "0"

    decimal = int(epsilon, 2)

    return decimal, epsilon


def find_matching_numbers(entries, index, match):
    numbers = []
    for entry in entries:
        if entry[index] == match:
            numbers.append(entry)

    return numbers


def calculate_oxygen_generator_rating(entries):
    numbers = entries
    for i in range(len(numbers[0])):
        g, gamma = calculate_gamma_rate(numbers)
        numbers = find_matching_numbers(numbers, i, gamma[i])
        if len(numbers) == 1:
            break

    decimal = int(numbers[0], 2)

    return decimal, numbers[0]


def calculate_cotwo_scrubber_rating(entries):
    numbers = entries
    for i in range(len(numbers[0])):
        g, gamma = calculate_gamma_rate(numbers)
        e, epsilon = calculate_epsilon_rate(gamma)
        numbers = find_matching_numbers(numbers, i, epsilon[i])
        if len(numbers) == 1:
            break

    decimal = int(numbers[0], 2)

    return decimal, numbers[0]
