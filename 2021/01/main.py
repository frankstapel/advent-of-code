import sys


def a(content: [str]) -> None:
    print(sum([1 for x in range(1, len(content)) if int(content[x]) > int(content[x - 1])]))


def b(content: [str]) -> None:
    print(sum([1 for x in range(len(content) - 2) if sum([int(y) for y in content[x+1:x+4]]) > sum([int(y) for y in content[x:x+3]])]))


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
