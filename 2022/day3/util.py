#
#
#

import string

def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    return entries

def split_entry(entry):
    return entry[:len(entry)//2], entry[len(entry)//2:]

def shared_item(first, second):
    return list(set(first) & set(second))[0]

def letter_to_priority(letter):
    letters = list(string.ascii_letters)
    return letters.index(letter) + 1

def sum_priorities(rucksacks):
    return sum([i['priority'] for i in rucksacks])

def make_rucksacks(entries):
    r = {
        'total': 0,
        'rucksacks': []
    }
    for entry in entries:
        first, second = split_entry(entry)
        shared = shared_item(first, second)
        priority = letter_to_priority(shared)
        r['rucksacks'].append({
            'first': first,
            'second': second,
            'shared': shared,
            'priority': priority,
        })

    r['total'] = sum_priorities(r['rucksacks'])

    return r
