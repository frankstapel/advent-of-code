import sys
import numpy as np
import networkx as nx


def a(content: [str]) -> None:
    grid = [list(line) for line in content]
    print(np.array(grid))
    start = (0, 0)
    end = (len(grid[0]) - 3, len(grid) - 1)
    connections = {}
    for y in range(len(grid)):
        for x, symbol in enumerate(grid[y]):
            if symbol != '#':
                connections[(x - 1, y)] = symbol

    print(connections)
    print(start, end)

    # Fill the graph
    G = nx.DiGraph()

    # Simplify the graph?

    # Find the longest path


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
