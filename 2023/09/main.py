import sys


def a(content: [str]) -> None:
    total = 0
    for line in content:
        current = [int(x) for x in line.split()]
        history = [current]
        while any(current):
            sequence = []
            for i in range(len(current) - 1):
                sequence.append(current[i + 1] - current[i])
            history.append(sequence)
            current = sequence
        history = history[::-1]
        mutation = 0
        for i in range(len(history)):
            new_mutation = history[i][-1] + mutation
            history[i].append(new_mutation)
            mutation = new_mutation
        total += history[-1][-1]
    print(total)


def b(content: [str]) -> None:
    total = 0
    for line in content:
        current = [int(x) for x in line.split()]
        history = [current]
        while any(current):
            sequence = []
            for i in range(len(current) - 1):
                sequence.append(current[i + 1] - current[i])
            history.append(sequence)
            current = sequence
        history = history[::-1]
        mutation = 0
        for i in range(len(history)):
            new_mutation = history[i][0] - mutation
            history[i] = [new_mutation] + history[i]
            mutation = new_mutation
        total += history[-1][0]
    print(total)


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
