#
#
#

import math


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    e = []
    for entry in entries:
        j = []
        for elem in list(entry):
            j.append(int(elem))
        e.append(j)

    return e


def visible_left(row, col, entries):
    visible = {'visible': True, 'trees': 0}
    for elem in entries[row][col-1::-1]:
        visible['trees'] += 1
        if elem >= entries[row][col]:
            visible['visible'] = False
            return visible
    return visible


def visible_right(row, col, entries):
    visible = {'visible': True, 'trees': 0}
    for elem in entries[row][col+1::1]:
        visible['trees'] += 1
        if elem >= entries[row][col]:
            visible['visible'] = False
            return visible
    return visible


def visible_up(row, col, entries):
    return visible_left(col, row, list(zip(*entries)))


def visible_down(row, col, entries):
    return visible_right(col, row, list(zip(*entries)))


def visible_element(row, col, entries):
    # Determine directions of visiblity
    vl = visible_left(row, col, entries)
    vr = visible_right(row, col, entries)
    vu = visible_up(row, col, entries)
    vd = visible_down(row, col, entries)

    # Collect directions in which tree is visible
    directions = []
    if vl['visible']:
        directions.append('left')
    if vr['visible']:
        directions.append('right')
    if vu['visible']:
        directions.append('up')
    if vd['visible']:
        directions.append('down')

    # Collect trees per direction
    tree_score = []
    for d in [vl, vr, vu, vd]:
        if d['trees'] > 0:
            tree_score.append(d['trees'])

    return {
        'directions': directions,
        'scenic_score': math.prod(tree_score)
    }


def find_visible_trees(entries):
    visible = 0
    top_tree = {'score': 0, 'row': 0, 'col': 0}
    for row, entry in enumerate(entries):
        for col, elem in enumerate(entry):
            # First row or last col always visible
            if row == 0 or col == 0:
                visible += 1
            # Last row or last col always visible
            elif row == (len(entries) - 1) or col == (len(entry) - 1):
                visible += 1
            # Test neither first/last row or first/last col
            elif (v := visible_element(row, col, entries))['directions']:
                if v['scenic_score'] > top_tree['score']:
                    top_tree = {
                        'score': v['scenic_score'],
                        'row': row,
                        'col': col
                    }
                visible += 1

    return visible, top_tree
