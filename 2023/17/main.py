import sys
import numpy as np
import heapq


def manhattan_distance(a, b) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def a(content: [str]) -> None:
    grid = {}
    queue = []
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
                    'previous': []
                }
                queue.append(key)
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
                        queue.append(key)

    solution_found = False
    while queue and not solution_found:
        # Pick the node with the lowest current distance
        node = None
        min_f_score = np.inf
        for queue_node in queue:
            if grid[queue_node]['f_score'] <= min_f_score:
                min_f_score = grid[queue_node]['f_score']
                node = queue_node
        queue.remove(node)
        
        # Go over the node's neighbors
        for permutation in permutations:
            # Don't go directly back!
            backwards_direction = (node[1][0] * -1, node[1][1] * -1)
            if permutation == backwards_direction:
                continue

            neighbor_position = (node[0][0] + permutation[0], node[0][1] + permutation[1])
            steps = node[2] + 1 if permutation == node[1] else 0
            neighbor = (neighbor_position, permutation, steps)

            if not neighbor in queue:
                continue

            new_distance = grid[node]['distance'] + grid[neighbor]['cost']

            if new_distance < grid[neighbor]['distance']:
                grid[neighbor]['distance'] = new_distance
                grid[neighbor]['f_score'] = grid[neighbor]['distance'] + grid[neighbor]['heuristic']
                grid[neighbor]['previous'] = grid[node]['previous'] + [node]

                if neighbor[0] == end:
                    solution_found = True
                    print(grid[neighbor]['distance'])
    
    # min_distance = np.inf
    # min_key = None
    # for key in grid.keys():
    #     if key[0] == (len(content[0]) - 1, len(content) - 1):
    #         min_distance = min(min_distance, grid[key]['distance'])
    #         if min_distance == grid[key]['distance']:
    #             min_key = key
    
    # for previous in grid[min_key]['previous']:
    #     print(previous[0])

    # print(min_distance)
    # # print(grid[(len(content[0]) - 1, len(content) - 1)]['previous'])


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
