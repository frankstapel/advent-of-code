import sys
import numpy as np


def a(content: [str]) -> None:
    current = (0, 0)
    trench = set()
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
        direction, length, _ = line.split()
        for _ in range(int(length)):
            current = (current[0] + moves[direction][0], current[1] + moves[direction][1])
            min_x = min(min_x, current[0])
            min_y = min(min_y, current[1])
            max_x = max(max_x, current[0])
            max_y = max(max_y, current[1])
            trench.add(current)
            volume += 1

    # Dig the interior
    for y in range(min_y, max_y + 1):
        inside = False
        last_trench = -np.inf
        first_trench = None
        for x in range(min_x, max_x + 1):
            if (x, y) in trench:
                if last_trench != x - 1:
                    first_trench = (x, y + 1) in trench
                last_trench = x
            else:
                # Passed a trench, check if we need to flip inside
                if last_trench == x - 1 and ((x - 2, y) not in trench or first_trench is not ((x - 1, y + 1) in trench)):
                    inside = not inside
                if inside:
                    volume += 1
    print(volume)


def b(content: [str]) -> None:
    moves = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    
    directions = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U'
    }
    
    transitions = {
        ('U', 'R'): (0, 1),
        ('R', 'U'): (0, 1),
        ('R', 'D'): (1, 1),
        ('D', 'R'): (1, 1),
        ('D', 'L'): (1, 0),
        ('L', 'D'): (1, 0),
        ('L', 'U'): (0, 0),
        ('U', 'L'): (0, 0),
    }
    
    corners = []
    current = (0, 0)
    for line in content:
        instruction = line.split()[2][2:-1]
        direction = directions[instruction[5]]
        length = int(instruction[:5], 16)
        current = (current[0] + moves[direction][0] * length, current[1] + moves[direction][1] * length)
        corners.append((current, direction))

    # Expand the corners so trenches are fully taken into account in surface calculation
    border_corners = []
    for index, (corner, direction) in enumerate(corners):
        next_direction = corners[index + 1][1] if index < len(corners) - 1 else corners[0][1]
        transition = transitions[(direction, next_direction)]
        border_corners.append((corner[0] + transition[0], corner[1] + transition[1]))
    
    # Apply the shoelace formula to calculate the surface between the border corners
    volume = 0
    current = border_corners[-1]
    for corner in border_corners:
        volume += current[0] * corner[1] - current[1] * corner[0]
        current = corner
    
    print(abs(int(volume * 0.5)))


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
