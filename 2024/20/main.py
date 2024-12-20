import sys


def a(content: [str]) -> None:
    track = set()
    possible_cheats = set()
    start = None
    end = None
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            if c in ".SE":
                track.add((x, y))
            if c == "S":
                start = (x, y)
            if c == "E":
                end = (x, y)
            if c == "#" and y > 0 and y < len(content) - 1 and x > 0 and x < len(line) -1:
                possible_cheats.add((x, y))
    
    


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
