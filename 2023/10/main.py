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
    # Manual selection of first step :')
    current = (s[0], s[1] + 1)
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


def b(content: [str]) -> None:
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
    # Manual selection of first step :')
    current = (s[0], s[1] + 1)
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

    pipeline = [current]
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
        pipeline.append(current)
    print(pipeline)


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
