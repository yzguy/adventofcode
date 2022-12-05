#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    entries = [entry.split(',') for entry in entries]

    return entries

def derange(d):
    elems = d.split('-')
    return list(range(int(elems[0]), int(elems[1])+1))

def overlaps(left, right):
   ov = False 
   if all(item in left for item in right):
       return True
   elif all(item in right for item in left):
       return True

   return ov

def derange_entries(entries):
    e = []
    for entry in entries:
        left, right = derange(entry[0]), derange(entry[1])
        e.append({
            'left': left,
            'right': right,
            'overlap': overlaps(left, right)
        })

    return e
