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

    total_distance = 0

    # For each node, loop over the remaining nodes and calculate the distance
    for a in range(len(nodes) - 1):
        for b in range(a + 1, len(nodes)):
            total_distance += calculate_distance(nodes[a], nodes[b])

    print(total_distance)


def b(content: [str]) -> None:
    print(content)


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
