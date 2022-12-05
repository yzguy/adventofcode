#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        entries = reader.read().splitlines()

    entries = [entry.split(",") for entry in entries]

    return entries


def derange(d):
    elems = d.split("-")
    return list(range(int(elems[0]), int(elems[1]) + 1))


def all_overlaps(left, right):
    ov = False
    if all(item in left for item in right):
        return True
    elif all(item in right for item in left):
        return True

    return ov


def any_overlaps(left, right):
    ov = False
    if any(item in left for item in right):
        return True
    elif any(item in right for item in left):
        return True

    return ov


def overlap_count(entries):
    return len([entry["overlap"] for entry in entries if entry["overlap"]])


def derange_entries(entries, any=False):
    e = {"count": 0, "entries": []}
    for entry in entries:
        left, right = derange(entry[0]), derange(entry[1])
        overlaps = any_overlaps(left, right) if any else all_overlaps(left, right)
        e["entries"].append(
            {
                "left": left,
                "right": right,
                "overlap": overlaps,
            }
        )
    e["count"] = overlap_count(e["entries"])

    return e
