import sys
from functools import reduce


def a(content: [str]) -> None:
    directions = list(content[0])
    instructions = {}
    for instruction in content[2:]:
        source, target = instruction.split(" = ")
        left, right = target[1:-1].split(", ")
        instructions[source] = {
            'L': left,
            'R': right
        }

    current = 'AAA'
    steps = 0
    while True:
        for direction in directions:
            current = instructions[current][direction]
            steps += 1
            if current == 'ZZZ':
                print(steps)
                return


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a, b):
    return a / gcd(a, b) * b


def b(content):
    directions = list(content[0])
    instructions = {}
    current = []
    for instruction in content[2:]:
        source, target = instruction.split(" = ")
        left, right = target[1:-1].split(", ")
        instructions[source] = {
            'L': left,
            'R': right
        }
        if source[2] == 'A':
            current.append(source)

    z_steps = []
    for node in current:
        steps = 0
        z_found = False
        while not z_found:
            for direction in directions:
                if z_found:
                    break
                node = instructions[node][direction]
                steps += 1
                if node[2] == 'Z':
                    z_found = True
        z_steps.append(steps)

    print(int(reduce(lcm, z_steps)))


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
