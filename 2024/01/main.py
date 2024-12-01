import sys


def a(content: [str]) -> None:
    left = []
    right = []
    for line in content:
        left_id, right_id = line.split("   ")
        left.append(int(left_id))
        right.append(int(right_id))
    left = sorted(left)
    right = sorted(right)
    print(sum([abs(left[i] - right[i]) for i in range(len(left))]))


def b(content: [str]) -> None:
    left = []
    right = []
    for line in content:
        left_id, right_id = line.split("   ")
        left.append(int(left_id))
        right.append(int(right_id))
    counts = {}
    for right_id in right:
        if right_id not in counts:
            counts[right_id] = 1
        else:
            counts[right_id] += 1
    print(sum([left_id * counts[left_id] if left_id in counts else 0 for left_id in left]))


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
