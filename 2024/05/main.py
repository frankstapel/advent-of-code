import sys


def a(content: [str]) -> None:
    previous_numbers = {}
    middle_numbers = []
    for line in content:
        if "|" in line:
            before, after = map(int, line.split("|"))
            if after not in previous_numbers:
                previous_numbers[after] = set()
            previous_numbers[after].add(before)

        if "," in line:
            numbers = list(map(int, line.split(",")))
            all_numbers = set(numbers)
            passed_numbers = set()
            valid = True
            for number in numbers:
                if number in previous_numbers:
                    for previous_number in previous_numbers[number]:
                        if (
                            previous_number in all_numbers
                            and previous_number not in passed_numbers
                        ):
                            valid = False
                            break
                passed_numbers.add(number)
            if valid:
                middle_numbers.append(numbers[len(numbers) // 2])
    print(sum(middle_numbers))


def b(content: [str]) -> None:
    previous_numbers = {}
    middle_numbers = []
    for line in content:
        if "|" in line:
            before, after = map(int, line.split("|"))
            if after not in previous_numbers:
                previous_numbers[after] = set()
            previous_numbers[after].add(before)

        if "," in line:
            numbers = list(map(int, line.split(",")))
            all_numbers = set(numbers)
            passed_numbers = set()
            valid = True
            for number in numbers:
                if number in previous_numbers:
                    for previous_number in previous_numbers[number]:
                        if (
                            previous_number in all_numbers
                            and previous_number not in passed_numbers
                        ):
                            valid = False
                            break
                passed_numbers.add(number)
            if not valid:
                dependencies = {}
                for number in numbers:
                    dependencies[number] = set()
                    for key, value in previous_numbers.items():
                        if number in value and key in all_numbers:
                            dependencies[number].add(key)
                final_order = []
                while len(final_order) < len(numbers):
                    for key, value in dependencies.items():
                        if value == set():
                            final_order.append(key)
                            dependencies.pop(key)
                            current = key
                            break
                    for key, value in dependencies.items():
                        value.discard(current)
                middle_numbers.append(final_order[len(final_order) // 2])
    print(sum(middle_numbers))


############################
### Start of boilerplate ###
############################


def parse_input(filename) -> [str]:
    with open(filename) as f:
        content = f.read().splitlines()
    return content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Please pass a puzzle part as argument")

    if len(sys.argv) > 2 and sys.argv[2].lower() in ["test", "-t", "t"]:
        filename = f"test_{sys.argv[1].lower()}.txt"
    else:
        filename = "input.txt"
    content = parse_input(filename)

    print(f"\nTesting part {sys.argv[1].upper()} on {filename}\n")

    if sys.argv[1].lower() == "a":
        a(content)
    elif sys.argv[1].lower() == "b":
        b(content)

    print("")
