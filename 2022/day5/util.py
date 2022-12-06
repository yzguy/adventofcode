#
#
#
import string


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    return entries


def parse_blocks(blocks):
    stacks = []
    for line in list(zip(*blocks)):
        if any(item in list(string.ascii_uppercase) for item in line):
            stacks.append(list(filter(lambda i: i.strip(), list(line)[::-1])))

    return stacks


def parse_procedures(procedures):
    p = []
    for procedure in procedures:
        parts = procedure.split(" ")
        p.append({
            "num": int(parts[1]),
            "from": int(parts[3]),
            "to": int(parts[5])
        })

    return p


def split_input(entries):
    split = entries.index("")
    blocks, procedures = entries[:split - 1], entries[split + 1:]

    blocks = parse_blocks(blocks)
    procedures = parse_procedures(procedures)

    return blocks, procedures


def run(entries):
    blocks, procedures = split_input(entries)
    for procedure in procedures:
        for i in range(procedure["num"]):
            letter = blocks[procedure["from"] - 1].pop()
            blocks[procedure["to"] - 1].append(letter)

    last = "".join([line.pop() for line in blocks])

    return last
