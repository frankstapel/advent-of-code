import sys


def f(springs: str, broken: str) -> int:
    print('Branching...')
    current = 0
    if broken == '[]':
        if '#' in springs:
            return 0
        else:
            return 1

    broken = [int(x) for x in broken[1:-1].split(', ')]

    if len(springs) < sum(broken) + len(broken) - 1:
        return 0

    possibilities = 0
    while springs:
        if not broken:
            if '#' in springs:
                return 0
            else:
                return 1

        spring = springs[0]
        springs = springs[1:]
        print(current, spring, springs, broken, possibilities)
        if spring == '#':
            # Add one to the current solution, check if it's still possible, else return 0
            current += 1
            if current > broken[0]:
                # print('#, no match')
                return possibilities
            # print('#, increasing current')
        if spring == '.':
            # Check if there is a current, otherwise just continue
            if current > 0:
                if current == broken[0]:
                    # Current matches the first broken exactly!
                    current = 0
                    broken = broken[1:]
                else:
                    # No match, return 0
                    # print('., no match')
                    return possibilities
            # print('. after .')
        if spring == '?':
            # Suppose it's a '#'
            if current + 1 > broken[0]:
                # It can't be a '#', so it must be a '.'
                if current == broken[0]:
                    # Current matches the first broken exactly!
                    current = 0
                    broken = broken[1:]
                    # print('?, must be ., matches')
                    return possibilities + f(springs, str(broken))
                else:
                    # print('?, must be ., no match')
                    return possibilities
            else:
                # It can be a '#', can it be a '.'?
                if current > 0 and current == broken[0]:
                    # Current matches the first broken exactly!
                    current = 0
                    broken = broken[1:]
                    # print('? can be both, branching')
                    possibilities += f(springs, str(broken))
                # Continue the current course, but add the possibility to the total where it is a '.'
                else:
                    if current == 0:
                        # print('?, branching . first')
                        possibilities += f(springs, str(broken))
                    # print('?, must be #')
                current += 1
    possibilities += 1
    return possibilities


def a(content: [str]) -> None:
    total = 0
    for line in content:
        print(f'\n\n\n\n\n\nSTARTING {line}')
        springs = line.split()[0]
        broken = [int(x) for x in line.split()[1].split(',')]
        x = f(springs, str(broken))
        print(x)
        total += x
    print(total)


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
