import sys
from math import prod


def process_part(part, workflow) -> str:
    for rule in workflow['rules']:
        if rule['comparison'] == '<' and part[rule['category']] < rule['threshold']:
            return rule['then']
        if rule['comparison'] == '>' and part[rule['category']] > rule['threshold']:
            return rule['then']
    return workflow['otherwise']


def a(content: [str]) -> None:
    workflow_lines = []
    part_lines = []
    workflows_parsed = False
    for line in content:
        if not workflows_parsed:
            if line == '':
                workflows_parsed = True
            else:
                workflow_lines.append(line)
        else:
            part_lines.append(line)

    # Fill the workflows
    workflows = {}
    for workflow_line in workflow_lines:
        key, values = workflow_line.split('{')
        values = values[:-1].split(',')
        rules = []
        for value in values[:-1]:
            threshold, then = value[2:].split(':')
            rules.append(
                {
                    'category': value[0],
                    'comparison': value[1],
                    'threshold': int(threshold),
                    'then': then
                }
            )
        workflows[key] = {
            'rules': rules,
            'otherwise': values[-1]
        }

    # Fill the parts
    parts = []
    for part_line in part_lines:
        part = {}
        for category in part_line[1:-1].split(','):
            key, value = category.split('=')
            part[key] = int(value)
        parts.append(part)

    # Process the parts
    total = 0
    for part in parts:
        key = 'in'
        terminated = False
        while not terminated:
            if key == 'A':
                total += sum(part.values())
                terminated = True
            elif key == 'R':
                terminated = True
            else:
                key = process_part(part, workflows[key])
    print(total)


def split_part(part, workflow):
    new_parts = []
    accepted = []
    remaining_part = part
    has_remaining_part = True
    for rule in workflow['rules']:
        if not has_remaining_part:
            break

        if rule['comparison'] == '<':
            if remaining_part[rule['category']][1] < rule['threshold']:
                new_part = remaining_part
                has_remaining_part = False
            elif rule['threshold'] < remaining_part[rule['category']][0]:
                continue
            else:
                new_remaining_part = remaining_part.copy()
                new_remaining_part[rule['category']] = (rule['threshold'], remaining_part[rule['category']][1])
                new_part = remaining_part.copy()
                new_part[rule['category']] = (remaining_part[rule['category']][0], rule['threshold'] - 1)
                remaining_part = new_remaining_part
        else:
            if remaining_part[rule['category']][0] > rule['threshold']:
                new_part = remaining_part
                has_remaining_part = False
            elif rule['threshold'] > remaining_part[rule['category']][1]:
                continue
            else:
                new_remaining_part = remaining_part.copy()
                new_remaining_part[rule['category']] = (new_remaining_part[rule['category']][0], rule['threshold'])
                new_part = remaining_part.copy()
                new_part[rule['category']] = (rule['threshold'] + 1, remaining_part[rule['category']][1])
                remaining_part = new_remaining_part

        if rule['then'] != 'R':
            if rule['then'] == 'A':
                accepted.append(new_part)
            else:
                new_parts.append((rule['then'], new_part))
    
    if has_remaining_part and workflow['otherwise'] != 'R':
        if workflow['otherwise'] == 'A':
            accepted.append(remaining_part)
        else:
            new_parts.append((
                workflow['otherwise'],
                remaining_part
            ))
    return new_parts, accepted


def b(content: [str]) -> None:
    workflow_lines = []
    part_lines = []
    workflows_parsed = False
    for line in content:
        if not workflows_parsed:
            if line == '':
                workflows_parsed = True
            else:
                workflow_lines.append(line)
        else:
            part_lines.append(line)

    # Fill the workflows
    workflows = {}
    for workflow_line in workflow_lines:
        key, values = workflow_line.split('{')
        values = values[:-1].split(',')
        rules = []
        for value in values[:-1]:
            threshold, then = value[2:].split(':')
            rules.append(
                {
                    'category': value[0],
                    'comparison': value[1],
                    'threshold': int(threshold),
                    'then': then
                }
            )
        workflows[key] = {
            'rules': rules,
            'otherwise': values[-1]
        }

    # Fill parts with the first part ranges
    parts = [('in', {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    })]

    # Process the part ranges
    total = 0
    while parts:
        popped_part = parts.pop()
        key, part = popped_part
        new_parts, accepted = split_part(part, workflows[key])
        parts = parts + new_parts
        total += sum([prod([range[1] - range[0] + 1 for range in part.values()]) for part in accepted])
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
