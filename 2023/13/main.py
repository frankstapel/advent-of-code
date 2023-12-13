import sys
import numpy as np


def a(content: [str]) -> None:
    patterns = []
    current_pattern = []
    for line in content:
        if line == '':
            patterns.append(current_pattern)
            current_pattern = []
        else:
            current_pattern.append(line)
    patterns.append(current_pattern)

    total = 0
    for pattern in patterns:
        current_rows = []
        symmetry_found = False
        for index, row in enumerate(pattern):
            current_rows = [row] + current_rows
            comparing_rows = pattern[index + 1:]
            compare = min(len(current_rows), len(comparing_rows))
            if compare > 0 and current_rows[:compare] == comparing_rows[:compare]:
                symmetry_found = True
                total += 100 * (index + 1)
                break

        if symmetry_found:
            continue

        pattern = list(np.array([list(row) for row in pattern]).T)
        pattern = [''.join(row) for row in pattern]

        current_rows = []
        for index, row in enumerate(pattern):
            current_rows = [row] + current_rows
            comparing_rows = pattern[index + 1:]
            compare = min(len(current_rows), len(comparing_rows))
            if compare > 0 and current_rows[:compare] == comparing_rows[:compare]:
                symmetry_found = True
                total += index + 1
                break
    print(total)


def compare_smudged(a: [str], b: [str]) -> bool:
    a = ''.join(a)
    b = ''.join(b)
    differences = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            differences += 1
            if differences > 1:
                return False
    return differences == 1


def b(content: [str]) -> None:
    patterns = []
    current_pattern = []
    for line in content:
        if line == '':
            patterns.append(current_pattern)
            current_pattern = []
        else:
            current_pattern.append(line)
    patterns.append(current_pattern)

    total = 0
    for pattern in patterns:
        current_rows = []
        symmetry_found = False
        for index, row in enumerate(pattern):
            current_rows = [row] + current_rows
            comparing_rows = pattern[index + 1:]
            compare = min(len(current_rows), len(comparing_rows))
            current_rows = current_rows[:compare]
            comparing_rows = comparing_rows[:compare]
            if compare > 0 and compare_smudged(current_rows[:compare], comparing_rows[:compare]):
                symmetry_found = True
                total += 100 * (index + 1)
                break

        if symmetry_found:
            continue

        pattern = list(np.array([list(row) for row in pattern]).T)
        pattern = [''.join(row) for row in pattern]

        current_rows = []
        for index, row in enumerate(pattern):
            current_rows = [row] + current_rows
            comparing_rows = pattern[index + 1:]
            compare = min(len(current_rows), len(comparing_rows))
            current_rows = current_rows[:compare]
            comparing_rows = comparing_rows[:compare]
            if compare > 0 and compare_smudged(current_rows[:compare], comparing_rows[:compare]):
                symmetry_found = True
                total += index + 1
                break
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
