import sys


def a(content: [str]) -> None:
    horizontal = depth = 0
    for instruction in content:
        direction, units = instruction.split(' ')
        units = int(units)
        match direction:
            case 'forward':
                horizontal += units
            case 'down':
                depth += units
            case 'up':
                depth -= units
    print(horizontal * depth)


def b(content: [str]) -> None:
    horizontal = depth = aim = 0
    for instruction in content:
        direction, units = instruction.split(' ')
        units = int(units)
        match direction:
            case 'forward':
                horizontal += units
                depth += aim * units
            case 'down':
                aim += units
            case 'up':
                aim -= units
    print(horizontal * depth)


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
