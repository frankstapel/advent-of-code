import sys


def a(content: [str]) -> None:
    values = {
        '2': 0,
        '3': 1,
        '4': 2,
        '5': 3,
        '6': 4,
        '7': 5,
        '8': 6,
        '9': 7,
        'T': 8,
        'J': 9,
        'Q': 10,
        'K': 11,
        'A': 12
    }

    five_of_a_kinds = []
    four_of_a_kinds = []
    full_houses = []
    three_of_a_kinds = []
    two_pairs = []
    pairs = []
    high_cards = []

    for line in content:
        cards = list(line.split()[0])
        hand = {
            'value': 0,
            'bid': int(line.split()[1])
        }

        ordering = [0 for _ in range(13)]
        for card_index, card in enumerate(cards[::-1]):
            ordering[values[card]] += 1
            hand['value'] += (15 ** card_index) * values[card]

        ordering = sorted(ordering, reverse=True)

        if ordering[0] == 5:
            five_of_a_kinds.append(hand)
        elif ordering[0] == 4:
            four_of_a_kinds.append(hand)
        elif ordering[0] == 3:
            if ordering[1] == 2:
                full_houses.append(hand)
            else:
                three_of_a_kinds.append(hand)
        elif ordering[0] == 2:
            if ordering[1] == 2:
                two_pairs.append(hand)
            else:
                pairs.append(hand)
        else:
            high_cards.append(hand)

    types = [five_of_a_kinds, four_of_a_kinds, full_houses,
             three_of_a_kinds, two_pairs, pairs, high_cards]

    ordered_hands = []
    for type in types[::-1]:
        ordered_hands += sorted(type, key=lambda x: x['value'])

    total = 0
    for rank, hand in enumerate(ordered_hands):
        total += (rank + 1) * hand['bid']
    print(total)


def b(content: [str]) -> None:
    values = {
        'J': 0,
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        'T': 9,
        'Q': 10,
        'K': 11,
        'A': 12
    }

    five_of_a_kinds = []
    four_of_a_kinds = []
    full_houses = []
    three_of_a_kinds = []
    two_pairs = []
    pairs = []
    high_cards = []

    for line in content:
        cards = list(line.split()[0])
        hand = {
            'cards': line.split()[0],
            'value': 0,
            'bid': int(line.split()[1])
        }

        ordering = [0 for _ in range(13)]
        for card_index, card in enumerate(cards[::-1]):
            ordering[values[card]] += 1
            hand['value'] += (15 ** card_index) * values[card]

        jokers = ordering[0]
        ordering = sorted(ordering[1:], reverse=True)

        if ordering[0] + jokers == 5:
            five_of_a_kinds.append(hand)
        elif ordering[0] + jokers == 4:
            four_of_a_kinds.append(hand)
        elif ordering[0] + jokers == 3:
            if ordering[1] == 2:
                full_houses.append(hand)
            else:
                three_of_a_kinds.append(hand)
        elif ordering[0] + jokers == 2:
            if ordering[1] == 2:
                two_pairs.append(hand)
            else:
                pairs.append(hand)
        else:
            high_cards.append(hand)

    types = [five_of_a_kinds, four_of_a_kinds, full_houses,
             three_of_a_kinds, two_pairs, pairs, high_cards]

    ordered_hands = []
    for type in types[::-1]:
        ordered_hands += sorted(type, key=lambda x: x['value'])

    total = 0
    for rank, hand in enumerate(ordered_hands):
        total += (rank + 1) * hand['bid']
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
