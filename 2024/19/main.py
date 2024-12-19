import sys
from functools import cache


def a(content: [str]) -> None:
    TOWELS = set(content[0].split(", "))

    @cache
    def is_possible(remaining_pattern) -> bool:
        if remaining_pattern == "":
            return True
        for towel in TOWELS:
            if remaining_pattern.startswith(towel):
                if is_possible(remaining_pattern[len(towel) :]):
                    return True
        return False

    possible_patterns = 0
    for pattern in content[2:]:
        if is_possible(pattern):
            possible_patterns += 1
    print(possible_patterns)


def b(content: [str]) -> None:
    TOWELS = set(content[0].split(", "))

    @cache
    def possibilities(remaining_pattern) -> int:
        if remaining_pattern == "":
            return 1
        count = 0
        for towel in TOWELS:
            if remaining_pattern.startswith(towel):
                count += possibilities(remaining_pattern[len(towel) :])
        return count

    possible_patterns = 0
    for pattern in content[2:]:
        possible_patterns += possibilities(pattern)
    print(possible_patterns)


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
