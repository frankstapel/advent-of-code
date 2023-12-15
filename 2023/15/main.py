import sys


def hash(label: str) -> int:
    current = 0
    for char in label:
        current += ord(char)
        current *= 17
        current %= 256
    return current


def a(content: [str]) -> None:
    steps = content[0].split(',')
    print(sum([hash(step) for step in steps]))


def b(content: [str]) -> None:
    steps = content[0].split(',')
    boxes = [[] for _ in range(256)]
    for step in steps:
        operation = '=' if '=' in step else '-'
        label, power = step.split(operation)
        box_index = hash(label)

        if operation == '=':
            lens_found = False
            for lens in boxes[box_index]:
                if lens['label'] == label:
                    lens_found = True
                    lens['power'] = int(power)
            
            if not lens_found:
                boxes[box_index].append({
                    'label': label,
                    'power': int(power)
                })
        else:
            remove_index = -1
            for lens_index, lens in enumerate(boxes[box_index]):
                if lens['label'] == label:
                    remove_index = lens_index
            
            if remove_index >= 0:
                del boxes[box_index][remove_index]
    
    total = 0
    for box_index, box in enumerate(boxes):
        for lens_index, lens in enumerate(box):
            total += (box_index + 1) * (lens_index + 1) * lens['power']
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
