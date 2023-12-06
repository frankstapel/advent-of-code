import sys


def a(content: [str]) -> None:
    times = content[0].split()[1:]
    distances = content[1].split()[1:]
    total = 1
    for race_index in range(len(times)):
        max_time = int(times[race_index])
        min_distance = int(distances[race_index])
        race_total = 0
        for hold in range(max_time):
            travel_duration = max_time - hold
            distance_traveled = travel_duration * hold
            if distance_traveled > min_distance:
                race_total += 1
        total *= race_total
    print(total)


def b(content: [str]) -> None:
    max_time = int(''.join(content[0].split()[1:]))
    min_distance = int(''.join(content[1].split()[1:]))
    race_total = 0
    for hold in range(max_time):
        travel_duration = max_time - hold
        distance_traveled = travel_duration * hold
        if distance_traveled > min_distance:
            race_total += 1
    print(race_total)


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
