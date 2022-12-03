#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    entries = [e.split() for e in entries]

    return entries


def play(opponent, me):
    options = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3,  # Scissors
        "X": 1,  # Rock
        "Y": 2,  # Paper
        "Z": 3,  # Scissors
        "LOSE": 0,
        "DRAW": 3,
        "WIN": 6,
    }
    points = options[me]

    # Rock < Paper
    if opponent == "A" and me == "Y":
        points += options["WIN"]
    # Paper < Scissors
    elif opponent == "B" and me == "Z":
        points += options["WIN"]
    # Scissors < Rock
    elif opponent == "C" and me == "X":
        points += options["WIN"]
    # Rock == Rock
    elif options[opponent] == options[me]:
        points += options["DRAW"]

    return points
