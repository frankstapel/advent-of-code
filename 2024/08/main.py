import sys
from itertools import combinations


def extend_antis(a, b, antis, antenna):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    x = a[0] - dx
    y = a[1] - dy
    if (x, y) in antis:
        antis[(x, y)].append(antenna)


def a(content: [str]) -> None:
    antennas = {}
    antis = {}
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            if c != ".":
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append((x, y))
            antis[(x, y)] = []

    for antenna, coords in antennas.items():
        for a, b in combinations(coords, 2):
            extend_antis(a, b, antis, antenna)
            extend_antis(b, a, antis, antenna)

    print(sum(1 for anti in antis.values() if len(anti) > 0))


def extend_antis_inf(a, b, antis, antenna):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    x, y = a
    while True:
        if (x, y) not in antis:
            return
        antis[(x, y)].add(antenna)
        x = x - dx
        y = y - dy


def b(content: [str]) -> None:
    antennas = {}
    antis = {}
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            if c != ".":
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append((x, y))
            antis[(x, y)] = set()

    for antenna, coords in antennas.items():
        for a, b in combinations(coords, 2):
            extend_antis_inf(a, b, antis, antenna)
            extend_antis_inf(b, a, antis, antenna)

    print(sum(1 for anti in antis.values() if len(anti) > 0))


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
