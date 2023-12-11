import sys
import numpy as np


def calculate_distance(a: int, b: int) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def a(content: [str]) -> None:
    # Expand the map vertically
    expanded_map = []
    for line in content:
        line = list(line)
        if '#' in line:
            expanded_map.append(line)
        else:
            # 2 rows of zeroes
            expanded_map.append(line)
            expanded_map.append(line)

    # Expand the map horizontally
    map = np.array(expanded_map).T
    expanded_map = []
    for line in map:
        if '#' in line:
            expanded_map.append(line)
        else:
            # 2 rows of zeroes
            expanded_map.append(line)
            expanded_map.append(line)
    map = expanded_map

    # Loop over all locations to find # coordinates
    nodes = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '#':
                nodes.append((x, y))

    # For each node, loop over the remaining nodes and calculate the distance
    total_distance = 0
    for a in range(len(nodes) - 1):
        for b in range(a + 1, len(nodes)):
            total_distance += calculate_distance(nodes[a], nodes[b])
    print(total_distance)


def calculate_galactic_distance(map, a: int, b: int, galaxy_size=1000000) -> int:
    distance = 0
    a, b = (min(a[0], b[0]), min(a[1], b[1])
            ), (max(a[0], b[0]), max(a[1], b[1]))

    # Start with a, follow the path, add 1 for not X, galaxy_size for X
    for x in range(1, b[0] - a[0]):
        if map[a[0] + x][a[1]] == 'X':
            distance += galaxy_size
        else:
            distance += 1
    for y in range(1, b[1] - a[1]):
        if map[a[0]][a[1] + y] == 'X':
            distance += galaxy_size
        else:
            distance += 1

    # Include corners
    if not (a[0] == b[0] or a[1] == b[1]):
        distance += 1

    # Include final node
    distance += 1
    return distance


def b(content: [str]) -> None:
    # Expand the map vertically
    expanded_map = []
    for line in content:
        line = list(line)
        if '#' in line:
            expanded_map.append(line)
        else:
            # Expand the galaxy!
            expanded_map.append(['X' for _ in range(len(line))])

    # Expand the map horizontally
    map = np.array(expanded_map).T
    expanded_map = []
    for line in map:
        if '#' in line:
            expanded_map.append(line)
        else:
            # Expand the galaxy!
            expanded_map.append(['X' for _ in range(len(line))])
    map = np.array(expanded_map)

    # Loop over all locations to find # coordinates
    nodes = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '#':
                nodes.append((x, y))

    # For each node, loop over the remaining nodes and calculate the distance
    total_distance = 0
    for a in range(len(nodes) - 1):
        for b in range(a + 1, len(nodes)):
            total_distance += calculate_galactic_distance(
                map, nodes[a], nodes[b])
    print(total_distance)


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

    if len(sys.argv) > 2 and sys.argv[2].lower() in ['test', '-t', 't']:
        filename = f'test_{sys.argv[1].lower()}.txt'
    else:
        filename = 'input.txt'
    content = parse_input(filename)

    print(f'\nTesting part {sys.argv[1].upper()} on {filename}\n')

    if sys.argv[1].lower() == 'a':
        a(content)
    elif sys.argv[1].lower() == 'b':
        b(content)

    print('')
