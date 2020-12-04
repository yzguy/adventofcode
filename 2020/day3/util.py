#
#
#

# Input is 
# Width = 31
# Length = 323

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    return lines

def extend_line(lines, number):
    return [list(line * 100)  for line in lines]
