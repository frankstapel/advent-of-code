import sys
from tqdm import tqdm


def a(content: [str]) -> None:
    # Fill the modules
    modules = {}
    for line in content:
        key, value = line.split(' -> ')
        module_type = key[0]
        module_key = key[1:] if module_type != 'b' else key
        targets = value.split(', ')
        modules[module_key] = {
            'module_type': module_type,
            'state': False,
            'targets': targets
        }

    # Set up the conjunction modules
    for module_key, module_values in modules.items():
        for target in module_values['targets']:
            if target in modules.keys() and modules[target]['module_type'] == '&':
                if 'inputs' not in modules[target].keys():
                    modules[target]['inputs'] = {}
                modules[target]['inputs'][module_key] = False

    low_count = 0
    high_count = 0

    button_presses = 1000
    for _ in range(button_presses):
        queue = [('button', False, 'broadcaster')]
        while queue:
            (src_key, signal, target_key), queue = queue[0], queue[1:]

            if target_key not in modules.keys():
                continue

            module = modules[target_key]

            if module['module_type'] == 'b':
                # Count the button press
                if not signal:
                    low_count += 1
                else:
                    high_count += 1
                new_signal = signal
            elif module['module_type'] == '%' and not signal:
                # Low signal, flip state
                module['state'] = not module['state']
                new_signal = module['state']
            elif module['module_type'] == '&':
                module['inputs'][src_key] = signal
                new_signal = not all(module['inputs'].values())
            else:
                continue

            for target in module['targets']:
                queue.append((target_key, new_signal, target))
                if not new_signal:
                    low_count += 1
                else:
                    high_count += 1
    print(low_count * high_count)


def b(content: [str]) -> None:
    # Fill the modules
    modules = {}
    for line in content:
        key, value = line.split(' -> ')
        module_type = key[0]
        module_key = key[1:] if module_type != 'b' else key
        targets = value.split(', ')
        modules[module_key] = {
            'module_type': module_type,
            'state': False,
            'targets': targets
        }

    # Set up the conjunction modules
    for module_key, module_values in modules.items():
        for target in module_values['targets']:
            if target in modules.keys() and modules[target]['module_type'] == '&':
                if 'inputs' not in modules[target].keys():
                    modules[target]['inputs'] = {}
                modules[target]['inputs'][module_key] = False

    low_count = 0
    high_count = 0

    button_presses = 100000000000
    for button_presses in tqdm(range(button_presses)):
        queue = [('button', False, 'broadcaster')]
        while queue:
            (src_key, signal, target_key), queue = queue[0], queue[1:]

            # if target_key == 'tv':
            #     print(target_key)

            # if target_key == 'rx':
            #     print(target_key, signal)


            if not signal and target_key == 'rx':
                print(button_presses + 1)
                return

            if target_key not in modules.keys():
                continue

            module = modules[target_key]

            if module['module_type'] == 'b':
                # Count the button press
                if not signal:
                    low_count += 1
                else:
                    high_count += 1
                new_signal = signal
            elif module['module_type'] == '%' and not signal:
                # Low signal, flip state
                module['state'] = not module['state']
                new_signal = module['state']
            elif module['module_type'] == '&':
                module['inputs'][src_key] = signal
                new_signal = not all(module['inputs'].values())
            else:
                continue

            for target in module['targets']:
                queue.append((target_key, new_signal, target))
                if not new_signal:
                    low_count += 1
                else:
                    high_count += 1


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
