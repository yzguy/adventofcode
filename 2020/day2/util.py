#
#
#


def read_file_to_list(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()

    es = [line.split(" ") for line in lines]

    return es


def parse_entries(entries):
    parsed_entries = []
    for entry in entries:
        # Grab Lower + Upper limit
        limits = entry[0].split("-")

        # Remove : from letter
        letter = entry[1].replace(":", "")

        # Password
        password = entry[2]

        parsed_entry = {
            "limit": {
                "lower": int(limits[0]),
                "upper": int(limits[1]),
            },
            "letter": letter,
            "password": password,
        }

        parsed_entries.append(parsed_entry)

    return parsed_entries
