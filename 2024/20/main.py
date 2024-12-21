import sys


def left(position):
    return position[0] - 1, position[1]


def right(position):
    return position[0] + 1, position[1]


def up(position):
    return position[0], position[1] + 1


def down(position):
    return position[0], position[1] - 1


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
            if c == "#" and 0 < y < len(content) - 1 and 0 < x < len(line) - 1:
                possible_cheats.add((x, y))
    
    current = end
    neighbor_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    passed = set()
    cost_to_finish = {}
    current_cost = 0

    while True:
        cost_to_finish[current] = current_cost
        current_cost += 1
        passed.add(current)
        if current == start:
            break
        next_found = False
        for neighbor_delta in neighbor_deltas:
            next = (current[0] + neighbor_delta[0], current[1] + neighbor_delta[1])
            if next in track and next not in passed:
                current = next
                next_found = True
                break
        if not next_found:
            break

    cheats = {}
    for possible_cheat in possible_cheats:
        cheat = None
        if (l := left(possible_cheat)) in track and (r := right(possible_cheat)) in track:
            cheat = abs(cost_to_finish[l] - cost_to_finish[r])
        elif (u := up(possible_cheat)) in track and (d := down(possible_cheat)) in track:
            cheat = abs(cost_to_finish[u] - cost_to_finish[d])
        if cheat:
            cheat -= 2
            if cheat not in cheats:
                cheats[cheat] = 0
            cheats[cheat] += 1
    print(sum([count for cheat, count in cheats.items() if cheat >= 100]))


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
