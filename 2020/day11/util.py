#
#
#

import copy

def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    return lines

def parse_floorplan(rows):
    floorplan = []
    for rindex, row in enumerate(rows):
        r = []
        for cindex, column in enumerate(row):
            c = {
                'status': column,
                'coords': {
                    'column': cindex,
                    'row': rindex
                },
                'adjacent': adjacent_points(cindex, rindex, rows)
            }
            r.append(c)
        floorplan.append(r)

    return floorplan

def adjacent_points(x, y, entries):
    adjacent_points = {
        'up_left': [-1, -1],
        'up': [0, -1],
        'up_right': [1, -1],
        'left': [-1, 0],
        'right': [1, 0],
        'down_left': [-1, 1],
        'down': [0, 1],
        'down_right': [1, 1]
    }

    adjacent_locations = []
    for key, val in adjacent_points.items():
        try:
            a_x, a_y = (x + val[0]), (y + val[1])
            if a_x < 0 or a_y < 0:
                continue
            entries[a_y][a_x]
            adjacent_locations.append({
                'location': key,
                'coords': {
                    'column': a_x,
                    'row': a_y
                }
            })
        except IndexError:
            continue

    return adjacent_locations

def check_for_occupied_adjacent_seats(locations, floorplan):
    occupied_locations = []
    for location in locations:
        row = location['coords']['row']
        column = location['coords']['column']
        status = floorplan[row][column]['status']

        if status == '#':
            occupied_locations.append(location)

    return occupied_locations

def apply_rules_to_floorplan(floorplan):
    floorplan_copy = copy.deepcopy(floorplan)

    for rindex, row in enumerate(floorplan):
        for cindex, column in enumerate(row):
            occupied_locations = check_for_occupied_adjacent_seats(
                    column['adjacent'], floorplan)
            element = floorplan_copy[rindex][cindex]
            # Skip floor
            if column['status'] == '.':
                continue
            elif column['status'] == 'L':
                if not occupied_locations:
                    element['status'] = '#'
            elif column['status'] == '#':
                if len(occupied_locations) >= 4:
                    element['status'] = 'L'

    return floorplan_copy
