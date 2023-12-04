import sys


def a(content: [str]) -> None:
    max_counts = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    possible_id_count = 0

    for game in content:
        possible = True
        records = game.split(": ")
        id = int(records[0].split(" ")[1])
        print(id)
        for record in records[1].split("; "):
            counts = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for combination in record.split(", "):
                (number, color) = combination.split(" ")
                counts[color] += int(number)
            print(counts)
            for (color, number) in counts.items():
                if number > max_counts[color]:
                    print("impossible!")
                    possible = False
        if possible:
            possible_id_count += id
    print(possible_id_count)


def b(content: [str]) -> None:
    power_sum = 0

    for game in content:
        records = game.split(": ")
        counts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for record in records[1].split("; "):
            for combination in record.split(", "):
                (number, color) = combination.split(" ")
                if int(number) > counts[color]:
                    counts[color] = int(number)
            print(counts)
        power = 1
        for (color, number) in counts.items():
            power *= number
        power_sum += power
    print(power_sum)


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
