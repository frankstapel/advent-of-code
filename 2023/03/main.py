import sys


def a(content: [str]) -> None:
    # Step 1, make a 2d array where each cell represents the partial number it is part of
    content = [list(x) for x in content]

    # Step 2, Go over all digits, if a digit is found, complete it.
    # digits = {
    #     "12-20": {
    #         "coordinates": [[12, 20], [13, 20]],
    #         "value": "26"
    #     }
    # }
    digits = {}
    current_key = None
    for y_index, y in enumerate(content):
        for x_index, x in enumerate(y):
            if x.isdigit():
                if current_key:
                    digits[current_key]["coordinates"].append(
                        [x_index, y_index])
                    digits[current_key]["value"] += x
                else:
                    current_key = f'{x_index}-{y_index}'
                    digits[current_key] = {
                        "coordinates": [[x_index, y_index]],
                        "value": x
                    }
            else:
                # Dot or symbol, break of building current
                current_key = None

    # Step 3, Look around the complete digit for a symbol, if it is found, add it to the total
    total = 0
    permutations = [-1, 0, 1]
    special_characters = list("!@#$%^&*()-+?_=,<>/")
    for digit in digits.values():
        valid = False
        for x, y in digit["coordinates"]:
            for x_perm in permutations:
                for y_perm in permutations:
                    try:
                        if content[y + y_perm][x + x_perm] in special_characters:
                            valid = True
                    except:
                        pass  # <3 AOC for letting me do this stuff
        if valid:
            total += int(digit["value"])

    print(total)


def b(content: [str]) -> None:
    # Step 1, make a 2d array where each cell represents the partial number it is part of
    content = [list(x) for x in content]

    # Step 2, Go over all digits, if a digit is found, complete it.
    # digits = {
    #     "12-20": {
    #         "coordinates": [[12, 20], [13, 20]],
    #         "value": "26"
    #     }
    # }
    digits = {}
    current_key = None
    for y_index, y in enumerate(content):
        for x_index, x in enumerate(y):
            if x.isdigit():
                if current_key:
                    digits[current_key]["coordinates"].append(
                        [x_index, y_index])
                    digits[current_key]["value"] += x
                else:
                    current_key = f'{x_index}-{y_index}'
                    digits[current_key] = {
                        "coordinates": [[x_index, y_index]],
                        "value": x
                    }
            else:
                # Dot or symbol, break of building current
                current_key = None

    # Step 3, Look around the complete digit for a symbol, if it is found, add it to the total
    total = 0
    permutations = [-1, 0, 1]
    # gears = {
    #     "12-20": [26]
    # }
    gears = {}
    for digit in digits.values():
        current_gear_keys = []
        for x, y in digit["coordinates"]:
            for x_perm in permutations:
                for y_perm in permutations:
                    y_index = y + y_perm
                    x_index = x + x_perm
                    try:
                        if content[y_index][x_index] == "*":
                            # Found a gear! Add the current number to its list
                            key = f"{x_index}-{y_index}"
                            if not key in current_gear_keys:
                                if key in gears.keys():
                                    gears[key].append(int(digit["value"]))
                                else:
                                    gears[key] = [int(digit["value"])]
                                current_gear_keys.append(key)
                    except:
                        pass  # <3 AOC for letting me do this stuff

    # Step 4 check which gears have 2 numbers
    for values in gears.values():
        if len(values) == 2:
            total += values[0] * values[1]

    print(total)


############################
### Start of boilerplate ###
############################

def parse_input(filename) -> [str]:
    with open(filename) as f:
        content = f.read().splitlines()
    return content


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Please pass a puzzle part as argument')

    filename = f'{'test_' if len(sys.argv) > 2 and sys.argv[2].lower() in [
        'test', '-t', 't'] else ''}{sys.argv[1].lower()}.txt'
    content = parse_input(filename)

    print(f'\nTesting part {sys.argv[1].upper()} on {filename}\n')

    if sys.argv[1].lower() == 'a':
        a(content)
    elif sys.argv[1].lower() == 'b':
        b(content)

    print('')
