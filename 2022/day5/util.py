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
            "from": int(parts[3])-1,
            "to": int(parts[5])-1
        })

    return p


def split_input(entries):
    split = entries.index("")
    blocks, procedures = entries[:split - 1], entries[split + 1:]

    blocks = parse_blocks(blocks)
    procedures = parse_procedures(procedures)

    return blocks, procedures


def run(entries, upgrade=False):
    blocks, procedures = split_input(entries)
    for procedure in procedures:
        if not upgrade:
            for i in range(procedure["num"]):
                blocks[procedure["to"]].append(
                        blocks[procedure["from"]].pop())
        else:
            blocks[procedure["to"]].extend(
                    blocks[procedure["from"]][-procedure["num"]:])
            del blocks[procedure["from"]][-procedure["num"]:]

    last = "".join([line.pop() for line in blocks])

    return last
