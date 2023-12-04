import sys


def a(content: [str]) -> None:
    total = 0
    for line in content:
        line = " ".join(line.split())
        information = line.split(" | ")
        winning_numbers = information[0].split(": ")[1].split(" ")
        card_numbers = information[1].split(" ")
        winning_card_numbers = []
        for card_number in card_numbers:
            if card_number in winning_numbers:
                winning_card_numbers.append(card_number)
        if len(winning_card_numbers) > 0:
            total += 2 ** (len(winning_card_numbers) - 1)
    print(total)


def b(content: [str]) -> None:
    results = []
    content = content[::-1]
    for line_index, line in enumerate(content):
        line = " ".join(line.split())
        information = line.split(" | ")
        winning_numbers = information[0].split(": ")[1].split(" ")
        card_numbers = information[1].split(" ")
        winning_card_numbers = []
        for card_number in card_numbers:
            if card_number in winning_numbers:
                winning_card_numbers.append(card_number)
        card_score = 1
        if results and len(winning_card_numbers) > 0:
            card_score += sum(
                results[max(0, line_index - len(winning_card_numbers)):]
            )
        results.append(card_score)
    print(sum(results))


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

    filename = f'{'test_' if len(sys.argv) > 2 and sys.argv[2].lower() in [
        'test', '-t', 't'] else ''}{sys.argv[1].lower()}.txt'
    content = parse_input(filename)

    print(f'\nTesting part {sys.argv[1].upper()} on {filename}\n')

    if sys.argv[1].lower() == 'a':
        a(content)
    elif sys.argv[1].lower() == 'b':
        b(content)

    print('')
