import sys
import numpy as np


def energize_path(mirrors: np.ndarray, energized: np.ndarray, current: (int, int), direction: (int, int)):
    while 0 <= current[0] and current[0] < len(mirrors) and 0 <= current[1] and current[1] < len(mirrors[current[0]]):
        if direction not in energized[current[0]][current[1]]:
            energized[current[0]][current[1]].append(direction)
        else:
            # Prevent recursive loops
            return energized

        symbol = mirrors[current[0]][current[1]]
        if symbol == '-' and direction[0] == 0:
            # Split left
            energized = energize_path(mirrors, energized, (current[0] - 1, current[1]), (-1, 0))
            # Split right
            return energize_path(mirrors, energized, (current[0] + 1, current[1]), (1, 0))
        elif symbol == '|' and direction[1] == 0:
            # Split up
            energized = energize_path(mirrors, energized, (current[0], current[1] - 1), (0, -1))
            # Split down
            return energize_path(mirrors, energized, (current[0], current[1] + 1), (0, 1))
        elif symbol == '/':
            direction = (-1 * direction[1], -1 * direction[0])
        elif symbol == '\\':
            direction = (direction[1], direction[0])
        current = (current[0] + direction[0], current[1] + direction[1])
    return energized


def energize_configuration(mirrors: np.ndarray, start: (int, int) = (0, 0), direction: (int, int) = (1, 0)):
    energized = [[[] for _ in range(len(line))] for line in mirrors]
    energized = energize_path(mirrors, energized, start, direction)
    total = 0
    for line in energized:
        for directions in line:
            if len(directions) > 0:
                total += 1
    return total


def a(content: [str]) -> None:
    mirrors = [list(line) for line in content]
    mirrors = np.transpose(mirrors)
    print(energize_configuration(mirrors))


def b(content: [str]) -> None:
    mirrors = [list(line) for line in content]
    mirrors = np.transpose(mirrors)
    max_energy = 0
    for x in range(len(mirrors)):
        for y in range(len(mirrors[x])):
            if x == 0:
                max_energy = max(energize_configuration(mirrors, (x, y), (1, 0)), max_energy)
            if x == len(mirrors) - 1:
                max_energy = max(energize_configuration(mirrors, (x, y), (-1, 0)), max_energy)
            if y == 0:
                max_energy = max(energize_configuration(mirrors, (x, y), (0, 1)), max_energy)
            if x == len(mirrors[x]) - 1:
                max_energy = max(energize_configuration(mirrors, (x, y), (0, -1)), max_energy)
    print(max_energy)


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
