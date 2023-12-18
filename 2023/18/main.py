import sys
import numpy as np
from tqdm import tqdm


def a(content: [str]) -> None:
    current = (0, 0)
    trench = {}
    moves = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    min_x, min_y = np.inf, np.inf
    max_x, max_y = -np.inf, -np.inf
    volume = 0

    # Dig the trench
    for line in content:
        direction, length, color = line.split()
        for _ in range(int(length)):
            current = (current[0] + moves[direction][0], current[1] + moves[direction][1])
            min_x = min(min_x, current[0])
            min_y = min(min_y, current[1])
            max_x = max(max_x, current[0])
            max_y = max(max_y, current[1])
            trench[current] = color[2:-1]
            volume += 1
    
    grid = [['.' for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]

    # Dig the interior
    for y in range(min_y, max_y + 1):
        inside = False
        last_trench = -np.inf
        first_trench = None
        for x in range(min_x, max_x + 1):
            if (x, y) in trench.keys():
                if last_trench != x - 1:
                    # First point of the trench (L)
                    first_trench = (x, y + 1) in trench.keys()
                # else:
                last_trench = x
                grid[y - min_y][x - min_x] = '#'
            else:
                # Passed a trench, check if we need to flip inside
                if last_trench == x - 1 and ((x - 2, y) not in trench.keys() or first_trench is not ((x - 1, y + 1) in trench.keys())):
                    inside = not inside

                if inside:
                    volume += 1
                    grid[y - min_y][x - min_x] = '+'

    with open('output.txt', 'w') as file:
        for y, line in enumerate(grid):
            file.write(''.join(line))
            file.write('\n')

    print(volume)


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
