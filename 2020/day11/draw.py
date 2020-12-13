#
#
#

def draw(entries):
    for row in entries:
        line = [c['status'] for c in row]
        print(''.join(line))
    print()
