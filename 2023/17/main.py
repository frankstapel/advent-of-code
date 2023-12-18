import sys
import numpy as np
from queue import PriorityQueue


def manhattan_distance(a, b) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def a(content: [str]) -> None:
    grid = {}
    queue = PriorityQueue()
    max_step_distance = 3
    start = (0, 0)
    end = (len(content[0]) - 1, len(content) - 1)
    permutations = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    for y, line in enumerate(content):
        for x, cost in enumerate(line):
            heuristic = manhattan_distance((x, y), end)
            if (x, y) == start:
                key = (start, (0, 0), 0)
                grid[key] = {
                    'cost': int(cost),
                    'distance': 0,
                    'heuristic': heuristic,
                    'f_score': heuristic,
                }
                queue.put((heuristic, key))
            else:
                for permutation in permutations:
                    for step in range(max_step_distance):
                        key = ((x, y), permutation, step)
                        grid[key] = {
                            'cost': int(cost),
                            'distance': np.inf,
                            'heuristic': heuristic,
                            'f_score': np.inf,
                        }
                        queue.put((np.inf, key))

    while queue:
        # Pick the node with the lowest current distance
        node = queue.get()[1]
        
        # Go over the node's neighbors
        for permutation in permutations:
            # Don't go directly back!
            backwards_direction = (node[1][0] * -1, node[1][1] * -1)
            if permutation == backwards_direction:
                continue

            neighbor_position = (node[0][0] + permutation[0], node[0][1] + permutation[1])
            steps = node[2] + 1 if permutation == node[1] else 0
            neighbor = (neighbor_position, permutation, steps)

            if not neighbor in grid.keys():
                continue

            new_distance = grid[node]['distance'] + grid[neighbor]['cost']
            if new_distance < grid[neighbor]['distance']:
                grid[neighbor]['distance'] = new_distance
                grid[neighbor]['f_score'] = grid[neighbor]['distance'] + grid[neighbor]['heuristic']

                # Add new neighbor to the priority queue
                queue.put((grid[neighbor]['f_score'], neighbor))

                if neighbor[0] == end:
                    print(grid[neighbor]['distance'])
                    return


def b(content: [str]) -> None:
    grid = {}
    queue = PriorityQueue()
    min_step_distance = 3 # 4 - 1
    max_step_distance = 10
    start = (0, 0)
    end = (len(content[0]) - 1, len(content) - 1)
    permutations = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    for y, line in enumerate(content):
        for x, cost in enumerate(line):
            heuristic = manhattan_distance((x, y), end)
            if (x, y) == start:
                key = (start, (0, 0), 4)
                grid[key] = {
                    'cost': int(cost),
                    'distance': 0,
                    'heuristic': heuristic,
                    'f_score': heuristic,
                    'previous': []
                }
                queue.put((heuristic, key))
            else:
                for permutation in permutations:
                    for step in range(max_step_distance):
                        key = ((x, y), permutation, step)
                        grid[key] = {
                            'cost': int(cost),
                            'distance': np.inf,
                            'heuristic': heuristic,
                            'f_score': np.inf,
                            'previous': []
                        }
                        queue.put((np.inf, key))

    distances = []
    while queue.qsize() > 0:
        # Pick the node with the lowest current distance
        node = queue.get()[1]
        
        # Determine the valid neighbors for the current position
        if node[2] < min_step_distance:
            # If we haven't taken 4 steps, we must continue in this direction
            valid_permutations = [node[1]]
        else:
            valid_permutations = []
            for permutation in permutations:
                backwards_direction = (node[1][0] * -1, node[1][1] * -1)
                if permutation != backwards_direction:
                    valid_permutations.append(permutation)
        # Go over the node's neighbors
        for permutation in valid_permutations:
            # Don't go directly back!
            neighbor_position = (node[0][0] + permutation[0], node[0][1] + permutation[1])
            steps = node[2] + 1 if permutation == node[1] else 0
            neighbor = (neighbor_position, permutation, steps)

            if not neighbor in grid.keys():
                continue

            new_distance = grid[node]['distance'] + grid[neighbor]['cost']
            if new_distance < grid[neighbor]['distance']:
                grid[neighbor]['distance'] = new_distance
                grid[neighbor]['f_score'] = grid[neighbor]['distance'] + grid[neighbor]['heuristic']
                grid[neighbor]['previous'] = grid[node]['previous'] + [node]

                # Add new neighbor to the priority queue
                queue.put((grid[neighbor]['f_score'], neighbor))

                if neighbor[0] == end and neighbor[2] >= min_step_distance:
                    distances.append(grid[neighbor]['distance'])
                    print(grid[neighbor]['distance'])
                    return


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
