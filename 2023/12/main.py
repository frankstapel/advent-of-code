import sys
from functools import cache


@cache # Bless Python for this function
def calculate_possibilities(springs: str, broken: str, current: int = 0) -> int:
    # Store broken as string so hashable function arguments can be cached!
        
    if broken == '[]':
        return 0 if '#' in springs else 1

    broken = [int(x) for x in broken[1:-1].split(', ')]

    if len(springs) + current < sum(broken) + len(broken) - 1:
        # Remaining springs are too few to fit broken
        return 0

    while springs:
        if not broken:
            return 0 if '#' in springs else 1

        spring, springs = springs[0], springs[1:]

        if spring == '#':
            # Add one to the current count
            current += 1
            if current > broken[0]:
                # Current count is not possible
                return 0
        elif spring == '.':
            if current > 0:
                # There is a current to handle
                if current == broken[0]:
                    # Current matches the first of broken exactly!
                    current = 0
                    broken = broken[1:]
                else:
                    # Current doesn't match
                    return 0
            elif len(springs) + current < sum(broken) + len(broken) - 1:
                # Remaining springs are too few to fit broken
                return 0
        elif spring == '?':
            # Time to split!
            damaged = calculate_possibilities('#' + springs, str(broken), current)
            operational = calculate_possibilities('.' + springs, str(broken), current)
            return damaged + operational
    
    return 1


def a(content: [str]) -> None:
    total_possibilities = 0
    for line in content:
        springs = line.split()[0]
        broken = str([int(x) for x in line.split()[1].split(',')])
        possibilities = calculate_possibilities(springs, broken)
        total_possibilities += possibilities
    print(total_possibilities)


def b(content: [str]) -> None:
    total_possibilities = 0
    for line in content:
        springs = '?'.join([line.split()[0] for _ in range(5)])
        five_times_broken = ','.join([line.split()[1] for _ in range(5)])
        broken = str([int(x) for x in five_times_broken.split(',')])
        possibilities = calculate_possibilities(springs, broken)
        total_possibilities += possibilities
    print(total_possibilities)


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
