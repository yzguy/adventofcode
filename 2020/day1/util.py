
def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()
    entries = [int(entry) for entry in entries]

    return entries


