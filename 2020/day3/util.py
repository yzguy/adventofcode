#
#
#

# Input is 
# Width = 31
# Length = 323

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    entries = extend_line(lines)

    return entries

def extend_line(lines):
    return [list(line * int((len(lines) / 3))) for line in lines] 
