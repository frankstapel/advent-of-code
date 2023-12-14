import sys
import numpy as np


def a(content: [str]) -> None:
    grid = np.array([list(line) for line in content])
    # Face grid north
    grid = np.rot90(grid)

    total = 0
    for row in grid:
        current_value = len(row)
        for index, element in enumerate(row):
            if element == 'O':
                total += current_value
                current_value -= 1
            elif element == '#':
                current_value = len(row) - index - 1

    print(total)


def move_grid(grid):
    new_grid = np.copy(grid)
    for row_index, row in enumerate(grid):
        current_index = 0
        for index, element in enumerate(row):
            if element == 'O':
                new_grid[row_index][index] = '.'
                new_grid[row_index][current_index] = 'O'
                current_index += 1
            elif element == '#':
                current_index = index + 1
    return new_grid


def calculate_load(grid):
    load = 0
    for row in grid:
        for index, element in enumerate(row):
            if element == 'O':
                load += len(row) - index
    return load


def b(content: [str]) -> None:
    number_of_cycles = 1000000000

    grid = np.array([list(line) for line in content])
    # Face grid east so it rotates into north on the first cycle
    grid = np.rot90(grid, 2)

    solutions = []
    loads = []
    for cycle_index in range(number_of_cycles):
        for _ in range(4):
            grid = np.rot90(grid, 3)
            grid = move_grid(grid)
        
        # Look for patterns!
        for solution_index, solution in enumerate(solutions):
            if np.array_equiv(solution, grid):
                # Found the pattern!
                print(loads[solution_index + (number_of_cycles - solution_index) % (cycle_index - solution_index) - 1])
                return
        
        # Append the current grid
        solutions.append(grid)

        # Calculate and append the north-pointing load
        north_grid = np.rot90(grid, 3)
        loads.append(calculate_load(north_grid))


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
