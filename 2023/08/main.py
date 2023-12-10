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


def b_1(content: [str]) -> None:
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
    print(current)

    steps = 0
    while True:
        for direction in directions:
            only_z = True
            for i in range(len(current)):
                current[i] = instructions[current[i]][direction]
                if current[i][2] != 'Z':
                    only_z = False
            steps += 1

            if only_z:
                print(steps)
                return


def b_2(content: [str]) -> None:
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

    values = {}
    start_end = {}

    for start in instructions.keys():
        # values[start] = [start[2] == 'Z']
        values[start] = []

    for start in instructions.keys():
        location = start
        for direction in directions:
            location = instructions[location][direction]
            values[start].append(location[2] == 'Z')
        start_end[start] = location

    print(current)
    steps = 0
    step_size = len(directions)
    while True:
        z_lists = []
        for i in range(len(current)):
            z_lists.append(values[current[i]])
            current[i] = start_end[current[i]]
        z_lists = np.transpose(z_lists)
        for step, z_list in enumerate(z_lists):
            if all(z_list):
                print(steps + step + 1)
                return
        steps += step_size


def b_3(content: [str]) -> None:
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

    # values = {}
    # start_end = {}

    # for start in instructions.keys():
    #     # values[start] = [start[2] == 'Z']
    #     values[start] = []

    maps = {

    }

    for start in instructions.keys():
        location = start
        z_indices = []
        for index, direction in enumerate(directions):
            location = instructions[location][direction]
            if location[2] == 'Z':
                z_indices.append(index)

        maps[start] = {
            'end': location,
            'zs': z_indices
        }

    print(maps)

    steps = 0
    step_size = len(directions)
    while True:
        zs = [0 for _ in range(step_size)]
        # print(f'\nCurrent: {current}')
        # print(f'Current step: {steps}')
        for i in range(len(current)):
            # print(maps[current[i]]['zs'])
            for z in maps[current[i]]['zs']:
                zs[z] += 1
                if zs[z] == len(current):
                    print('Match!')
                    print(len(current))
                    print(zs)
                    print(steps + z + 1)
                    return
            current[i] = maps[current[i]]['end']
        steps += step_size


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
    print(current)

    z_steps = []
    for node in current:
        steps = 0
        z_found = False
        while not z_found:
            for direction in directions:
                if z_found:
                    break
                # print(node)
                node = instructions[node][direction]
                # print(f'{node}\n')
                steps += 1
                if node[2] == 'Z':
                    z_found = True
        z_steps.append(steps)
    print(z_steps)

    # LCM over z_steps
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
