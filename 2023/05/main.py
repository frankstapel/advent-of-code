import sys


def a(content: [str]) -> None:
    seeds = [int(x) for x in content[0].split(": ")[1].split()]
    maps = []
    map = []
    for line in content[2:]:
        if line == '':
            continue
        if not line[:1].isdigit():
            # Append the old map and start a new one
            maps.append(map)
            map = []
        else:
            # Fill the map!
            # instruction = {
            #     'start': 0,
            #     'end': 0 + 37,
            #     'mutation': 15 - 0
            # }
            target, source, length = [int(x) for x in line.split()]
            map.append({
                'start': source,
                'end': source + length - 1,
                'mutation': target - source
            })
    maps.append(map)

    for i in range(len(seeds)):
        for map in maps:
            map_solved = False
            for instruction in map:
                if instruction['start'] <= seeds[i] and seeds[i] <= instruction['end'] and not map_solved:
                    seeds[i] += instruction['mutation']
                    map_solved = True
    print(min(seeds))


def b(content: [str]) -> None:
    initial_seeds = [int(x) for x in content[0].split(": ")[1].split()]
    seeds = []
    for i in range(len(initial_seeds)):
        if i % 2 == 0:
            seeds.append({
                'start': initial_seeds[i],
                'end': initial_seeds[i] + initial_seeds[i + 1] - 1
            })
    initial_seeds = seeds.copy()

    maps = []
    map = []
    for line in content[2:]:
        if line == '':
            continue
        if not line[:1].isdigit():
            # Append the old map and start a new one
            maps.append(map)
            map = []
        else:
            # Fill the map!
            # instruction = {
            #     'start': 0,
            #     'end': 0 + 37,
            #     'mutation': 15 - 0
            # }
            target, source, length = [int(x) for x in line.split()]
            map.append({
                'start': source,
                'end': source + length - 1,
                'mutation': target - source
            })
    maps.append(map)
    maps = maps[1:]

    for map in maps:
        handled_seeds = []
        while seeds:
            seed = seeds.pop()
            seed_handled = False
            for instruction in map:
                if seed_handled:
                    break
                if instruction['start'] <= seed['start'] and seed['start'] <= instruction['end']:
                    if instruction['start'] <= seed['end'] and seed['end'] <= instruction['end']:
                        # Seed is small enought, convert it!
                        seed['start'] += instruction['mutation']
                        seed['end'] += instruction['mutation']
                        handled_seeds.append(seed)
                    else:
                        # The seed goes on for too long, split it!
                        seeds.append({
                            'start': seed['start'],
                            'end': instruction['end']
                        })
                        seeds.append({
                            'start': instruction['end'] + 1,
                            'end': seed['end']
                        })
                    seed_handled = True
                elif instruction['start'] <= seed['end'] and seed['end'] <= instruction['end']:
                    # The seed starts too early, split it!
                    seeds.append({
                        'start': seed['start'],
                        'end': instruction['start'] - 1
                    })
                    seeds.append({
                        'start': instruction['start'],
                        'end': seed['end']
                    })
                    seed_handled = True
            if not seed_handled:
                handled_seeds.append(seed)
        seeds = handled_seeds

    # print(seeds)

    print(min([correct_seed['start'] for correct_seed in seeds]))

    # # Determine which seeds that are left over are in the original sets
    # correct_seeds = []
    # while seeds:
    #     seed = seeds.pop()
    #     seed_handled = False
    #     for initial_seed in initial_seeds:
    #         if seed_handled:
    #             break
    #         if initial_seed['start'] <= seed['start'] and seed['start'] <= initial_seed['end']:
    #             if initial_seed['start'] <= seed['end'] and seed['end'] <= initial_seed['end']:
    #                 # Seed fits in the initial seed!
    #                 correct_seeds.append(seed)
    #             else:
    #                 # The seed is too large, split it! TODO
    #                 seeds.append({
    #                     'start': seed['start'],
    #                     'end': initial_seed['end']
    #                 })
    #                 seeds.append({
    #                     'start': initial_seed['end'] + 1,
    #                     'end': seed['end']
    #                 })
    #             seed_handled = True
    # print(correct_seeds)

    # # Determine the minimal seed
    # print(min([correct_seed['start'] for correct_seed in correct_seeds]))


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

    # handled_seeds = []
    # while seeds:
    #     seed = seeds.pop()
    #     valid_seed = True
    #     print(seed)
    #     for map in maps:
    #         if not valid_seed:
    #             break
    #         map_solved = False
    #         for instruction in map:
    #             if not valid_seed:
    #                 break
    #             if instruction['start'] <= seed['start'] and seed['start'] < instruction['end'] and not map_solved:
    #                 if instruction['start'] <= seed['end'] and seed['end'] < instruction['end']:
    #                     # Seed is small enought, convert it! TODO
    #                     map_solved = True
    #                 else:
    #                     # The seed is too large, split it! TODO
    #                     valid_seed = False
    #     handled_seeds.append(seed)

    # for map in maps:
    #     handled_seeds = []
    #     while seeds:
    #         seed = seeds.pop()
    #         seed_handled = False
    #         for instruction in map:
    #             if seed_handled:
    #                 break
    #             if instruction['start'] <= seed['start'] and seed['start'] <= instruction['end']:
    #                 if instruction['start'] <= seed['end'] and seed['end'] <= instruction['end']:
    #                     # Seed is small enought, convert it!
    #                     seed['start'] += instruction['mutation']
    #                     seed['end'] += instruction['mutation']
    #                     handled_seeds.append(seed)
    #                 else:
    #                     # The seed is too large, split it! TODO
    #                     seeds.append({
    #                         'start': seed['start'],
    #                         'end': instruction['end']
    #                     })
    #                     seeds.append({
    #                         'start': instruction['end'] + 1,
    #                         'end': seed['end']
    #                     })
    #                 seed_handled = True
    #         if not seed_handled:
    #             handled_seeds.append(seed)
    #     seeds = handled_seeds
