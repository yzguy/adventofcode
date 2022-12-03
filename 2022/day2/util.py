#
#
#
OPTIONS = {
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


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    entries = [e.split() for e in entries]

    return entries


def play(opponent, me):
    points = OPTIONS[me]

    # Rock < Paper
    if opponent == "A" and me == "Y":
        points += OPTIONS["WIN"]
    # Paper < Scissors
    elif opponent == "B" and me == "Z":
        points += OPTIONS["WIN"]
    # Scissors < Rock
    elif opponent == "C" and me == "X":
        points += OPTIONS["WIN"]
    # Rock == Rock
    elif OPTIONS[opponent] == OPTIONS[me]:
        points += OPTIONS["DRAW"]

    return points


def strategy_guide(entries):
    # X = LOSE, Y = DRAW, Z = WIN
    results = {
        # Rock
        "A": {
            "X": "Z",  # Scissors
            "Y": "X",  # Rock
            "Z": "Y",  # Paper
        },
        # Paper
        "B": {
            "X": "X",  # Rock
            "Y": "Y",  # Paper
            "Z": "Z",  # Scissor
        },
        # Scissor
        "C": {
            "X": "Y",  # Paper
            "Y": "Z",  # Scissor
            "Z": "X",  # Rock
        },
    }
    e = [[entry[0], results[entry[0]][entry[1]]] for entry in entries]

    return e
