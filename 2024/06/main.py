import sys
from tqdm import tqdm


def a(content: [str]) -> None:
    grid = {}
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "^":
                grid[(x, y)] = "."
                current = (x, y, 0)

    dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

    passed_fields = set()
    passed_states = set()

    while True:
        if current in passed_states:
            break
        x, y, d = current
        passed_states.add(current)
        passed_fields.add((x, y))
        next = (x + dirs[d][0], y + dirs[d][1])

        if grid.get(next) == "#":
            d = (d + 1) % 4
            current = (x, y, d)
        elif grid.get(next) == ".":
            x, y = next
            current = (x, y, d)

    print(len(passed_fields))


def b(content: [str]) -> None:
    grid = {}
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "^":
                grid[(x, y)] = "."
                current = (x, y, 0)

    dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

    possible_obstructions = 0

    for x, y in tqdm(grid):
        if grid.get((x, y)) == "#" or current[:2] == (x, y):
            continue
        else:
            temp_grid = grid.copy()
            temp_current = current
            temp_grid[(x, y)] = "#"

        passed_fields = set()
        passed_states = set()

        out_of_bounds = False

        while True:
            if temp_current in passed_states:
                break
            x, y, d = temp_current
            passed_states.add(temp_current)
            passed_fields.add((x, y))
            next = (x + dirs[d][0], y + dirs[d][1])

            if temp_grid.get(next) == "#":
                d = (d + 1) % 4
                temp_current = (x, y, d)
            elif temp_grid.get(next) == ".":
                x, y = next
                temp_current = (x, y, d)
            else:
                out_of_bounds = True

        if not out_of_bounds:
            possible_obstructions += 1

    print(possible_obstructions)


############################
### Start of boilerplate ###
############################


def parse_input(filename) -> [str]:
    with open(filename) as f:
        content = f.read().splitlines()
    return content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Please pass a puzzle part as argument")

    if len(sys.argv) > 2 and sys.argv[2].lower() in ["test", "-t", "t"]:
        filename = f"test_{sys.argv[1].lower()}.txt"
    else:
        filename = "input.txt"
    content = parse_input(filename)

    print(f"\nTesting part {sys.argv[1].upper()} on {filename}\n")

    if sys.argv[1].lower() == "a":
        a(content)
    elif sys.argv[1].lower() == "b":
        b(content)

    print("")
