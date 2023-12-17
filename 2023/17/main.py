import sys
import numpy as np


def working_normal_dijkstra(content: [str]) -> None:
    grid = {}
    queue = []

    for y, line in enumerate(content):
        for x, cost in enumerate(line):
            grid[(x, y)] = {
                'cost': int(cost),
                'distance': np.inf,
                'previous': []
            }
            queue.append((x, y))
    
    grid[(0, 0)]['distance'] = 0
    permutations = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    while queue:
        # Pick the node with the lowest current distance
        node = None
        min_distance = np.inf
        for queue_node in queue:
            if grid[queue_node]['distance'] <= min_distance:
                min_distance = grid[queue_node]['distance']
                node = queue_node
        queue.remove(node)
        
        # Go over the node's neighbors
        for permutation in permutations:
            neighbor = (node[0] + permutation[0], node[1] + permutation[1])
            if not neighbor in queue:
                continue

            new_distance = grid[node]['distance'] + grid[neighbor]['cost']

            if new_distance < grid[neighbor]['distance']:
                grid[neighbor]['distance'] = new_distance
                grid[neighbor]['previous'] = grid[node]['previous'] + [node]
    
    print(grid[(len(content[0]) - 1, len(content) - 1)]['distance'])
    print(grid[(len(content[0]) - 1, len(content) - 1)]['previous'])


def brainfart(content: [str]) -> None:
    grid = {}
    queue = []
    max_step_distance = 3
    permutations = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    for y, line in enumerate(content):
        for x, cost in enumerate(line):
            grid[(x, y)] = {
                'cost': int(cost),
                'min_distance': np.inf
            }
            for permutation in permutations:
                grid[(x, y)][permutation] = [np.inf for _ in range(max_step_distance)]
            queue.append((x, y))

    for permutation in permutations:
        grid[(0, 0)]['min_distance'] = 0
        grid[(0, 0)][permutation][0] = 0
        # [0 for _ in range(max_step_distance)]

    for key, value in grid.items():
        print(key, value)

    count = 0
    while queue and count < 5:
        count += 1
        # Pick the node with the lowest current distance
        node = None
        min_distance = np.inf
        for queue_node in queue:
            if grid[queue_node]['min_distance'] <= min_distance:
                min_distance = grid[queue_node]['min_distance']
                node = queue_node
        queue.remove(node)

        print(node)
        
        # Go over the node's neighbors
        for permutation in permutations:
            # Determine the neighbor node
            neighbor = (node[0] + permutation[0], node[1] + permutation[1])
            
            # Continue if the neighbor doesn't exist
            if not neighbor in grid.keys():
                continue

            if not neighbor in queue:
                continue

            max_distance = grid[node][permutation][-1]
            print(max_distance)

            # Check if there is still room at the end of the permutation
            if max_distance != np.inf and max_distance:
                print('x')
                continue

            # Calculate the new distances
            new_distances = [np.inf] + [distance + grid[neighbor]['cost'] for distance in grid[node][permutation][:-1]]

            print(new_distances)
            print(grid[neighbor][permutation])

            for new_distance_index, new_distance in enumerate(new_distances):
                if new_distance < grid[neighbor][permutation][new_distance_index]:
                    grid[neighbor][permutation][new_distance_index] = new_distance

            print(grid[neighbor][permutation])

            # Update the minimum distance for the neighbor node
            grid[neighbor]['min_distance'] = min([grid[neighbor]['min_distance']] + grid[neighbor][permutation])
    
    print(grid[(len(content[0]) - 1, len(content) - 1)]['min_distance'])


def a(content: [str]) -> None:
    grid = {}
    queue = []

    for y, line in enumerate(content):
        for x, cost in enumerate(line):
            grid[(x, y)] = {
                'cost': int(cost),
                'distance': np.inf,
                'previous': [],
                'previous_permutations': []
            }
            queue.append((x, y))
    
    grid[(0, 0)]['distance'] = 0
    permutations = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    while queue:
        # Pick the node with the lowest current distance
        node = None
        min_distance = np.inf
        for queue_node in queue:
            if grid[queue_node]['distance'] <= min_distance:
                min_distance = grid[queue_node]['distance']
                node = queue_node
        queue.remove(node)
        
        # Go over the node's neighbors
        for permutation in permutations:
            neighbor = (node[0] + permutation[0], node[1] + permutation[1])

            # if not neighbor in queue:
            #     continue

            if not neighbor in grid.keys():
                continue

            new_distance = grid[node]['distance'] + grid[neighbor]['cost']

            # Check if this will be the fourth step in a direction, if so, continue
            equal_permutations = 0
            for previous_permutation in grid[node]['previous_permutations'][-3:]:
                equal_permutations += 1 if previous_permutation == permutation else 0

            if equal_permutations == 3:
                continue

            if new_distance < grid[neighbor]['distance']:
                grid[neighbor]['distance'] = new_distance
                grid[neighbor]['previous'] = grid[node]['previous'] + [node]
                grid[neighbor]['previous_permutations'] = grid[node]['previous_permutations'] + [permutation]

                # Neighbor changed! Add it to the queue if it's not in there
                if not neighbor in queue:
                    queue.append(neighbor)
    
    print(grid[(len(content[0]) - 1, len(content) - 1)]['distance'])
    print(grid[(len(content[0]) - 1, len(content) - 1)]['previous'])

    # This might be a step in the right direction. The problem is that the algorithm looks for a solution too locally.
    # It abides by the current rules, but could find a better solution if history was properly managed


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
