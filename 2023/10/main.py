import sys
import numpy as np


def a(content: [str]) -> None:
    # Create a 2d grid traversable with math coordinates
    grid = [list(line) for line in content]
    grid = np.transpose(grid)
    grid = [line[::-1] for line in grid]

    # Find S
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'S':
                s = (x, y)

    symbols = {
        '|': {
            'first': (0, -1),
            'second': (0, 1)
        },
        '-': {
            'first': (-1, 0),
            'second': (1, 0)
        },
        'L': {
            'first': (0, 1),
            'second': (1, 0)
        },
        'J': {
            'first': (0, 1),
            'second': (-1, 0)
        },
        '7': {
            'first': (-1, 0),
            'second': (0, -1)
        },
        'F': {
            'first': (1, 0),
            'second': (0, -1)
        }
    }

    # Follow the path and count the steps until S is found again
    previous = s
    try:
        if grid[s[0]][s[1] + 1] in ['|', '7', 'F']:
            current = (s[0], s[1] + 1)
    except:
        pass
    try:
        if grid[s[0]][s[1] - 1] in ['|', 'L', 'J']:
            current = (s[0], s[1] - 1)
    except:
        pass
    try:
        if grid[s[0] + 1][s[1]] in ['-', '7', 'J']:
            current = (s[0] + 1, s[1])
    except:
        pass
    try:
        if grid[s[0] - 1][s[1]] in ['-', 'L', 'F']:
            current = (s[0] - 1, s[1])
    except:
        pass

    steps = 1
    while True:
        if grid[current[0]][current[1]] == 'S':
            break
        # Follow the symbol
        symbol = symbols[grid[current[0]][current[1]]]
        first = symbol['first']
        second = symbol['second']
        if (current[0] + first[0], current[1] + first[1]) == previous:
            # Apply second
            previous = current
            current = (current[0] + second[0], current[1] + second[1])
        else:
            # Apply first
            previous = current
            current = (current[0] + first[0], current[1] + first[1])
        steps += 1

    # Split steps in half
    print(int(steps * 0.5))


def expand(x: int, y: int) -> (int, int):
    return 2 * x + 1, 2 * y + 1


def b(content: [str]) -> None:
    # Create a 2d grid traversable with math coordinates
    grid = [list(line) for line in content]
    grid = np.transpose(grid)
    grid = np.array([line[::-1] for line in grid])

    # Create an expanded target 2d array
    expanded_grid = np.ones(expand(len(grid), len(grid[0])))

    # Find S
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'S':
                s = (x, y)

    symbols = {
        '|': {
            'first': (0, -1),
            'second': (0, 1)
        },
        '-': {
            'first': (-1, 0),
            'second': (1, 0)
        },
        'L': {
            'first': (0, 1),
            'second': (1, 0)
        },
        'J': {
            'first': (0, 1),
            'second': (-1, 0)
        },
        '7': {
            'first': (-1, 0),
            'second': (0, -1)
        },
        'F': {
            'first': (1, 0),
            'second': (0, -1)
        }
    }

    # Follow the path and count the steps until S is found again
    previous = s
    try:
        if grid[s[0]][s[1] + 1] in ['|', '7', 'F']:
            current = (s[0], s[1] + 1)
    except:
        pass
    try:
        if grid[s[0]][s[1] - 1] in ['|', 'L', 'J']:
            current = (s[0], s[1] - 1)
    except:
        pass
    try:
        if grid[s[0] + 1][s[1]] in ['-', '7', 'J']:
            current = (s[0] + 1, s[1])
    except:
        pass
    try:
        if grid[s[0] - 1][s[1]] in ['-', 'L', 'F']:
            current = (s[0] - 1, s[1])
    except:
        pass

    expanded_start = expand(current[0], current[1])
    expanded_grid[expanded_start[0]][expanded_start[1]] = 0
    while True:
        if grid[current[0]][current[1]] == 'S':
            break
        # Follow the symbol
        symbol = symbols[grid[current[0]][current[1]]]
        first = symbol['first']
        second = symbol['second']
        if (current[0] + first[0], current[1] + first[1]) == previous:
            # Apply second
            expanded_current = expand(current[0], current[1])
            expanded_filler = (
                expanded_current[0] + second[0], expanded_current[1] + second[1])
            previous = current
            current = (current[0] + second[0], current[1] + second[1])
            # Fill the expanded grid
            expanded_current = expand(current[0], current[1])
        else:
            # Apply first
            expanded_current = expand(current[0], current[1])
            expanded_filler = (
                expanded_current[0] + first[0], expanded_current[1] + first[1])
            previous = current
            current = (current[0] + first[0], current[1] + first[1])
            # Fill the expanded grid
            expanded_current = expand(current[0], current[1])
        expanded_grid[expanded_filler[0]][expanded_filler[1]] = 0
        expanded_grid[expanded_current[0]][expanded_current[1]] = 0

    # Connect the end to the start!
    connection = (
        (expanded_current[0] + expanded_start[0]) // 2,
        (expanded_current[1] + expanded_start[1]) // 2
    )
    expanded_grid[connection[0]][connection[1]] = 0

    queue = [(0, 0)]
    sides = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        current = queue.pop()
        for side in sides:
            node_to_check = (current[0] + side[0], current[1] + side[1])
            if (
                node_to_check[0] >= 0
                and node_to_check[0] < len(expanded_grid)
                and node_to_check[1] >= 0
                and node_to_check[1] < len(expanded_grid[0])
                and expanded_grid[node_to_check[0]][node_to_check[1]] > 0
                and not node_to_check in queue
            ):
                # This node is outside! Add it to the queue
                queue.append(node_to_check)
        expanded_grid[current[0]][current[1]] = 0

    # Loop over the original plan and count all 0s
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            expanded = expand(x, y)
            count += expanded_grid[expanded[0]][expanded[1]]
    print(int(count))


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
