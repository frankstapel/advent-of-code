import sys


PERMUTATIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


cache = {}


def take_steps(mapping, current, steps):
    key = (current, steps)

    if key in cache.keys():
        return cache[key]

    if not current in mapping.keys():
        cache[key] = None
    elif mapping[current] == '#':
        cache[key] = None
    elif steps == 0:
        cache[key] = {current}
    else:
        possible_nodes = set()
        for permutation in PERMUTATIONS:
            neighbor = (current[0] + permutation[0],
                        current[1] + permutation[1])
            neighbor_nodes = take_steps(mapping, neighbor, steps - 1)
            if neighbor_nodes:
                possible_nodes = possible_nodes.union(neighbor_nodes)
        cache[key] = possible_nodes
    return cache[key]


def a(content: [str]) -> None:
    grid = [list(line) for line in content]
    mapping = {}
    start = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            mapping[(x, y)] = grid[y][x]
            if mapping[(x, y)] == 'S':
                start = (x, y)
    remaining_nodes = take_steps(mapping, start, 64)
    print(remaining_nodes)
    print(len(remaining_nodes))


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
