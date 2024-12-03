import sys
import re


def a(content: [str]) -> None:
    total = 0
    for line in content:
        total += sum(
            [
                int(x[4:-1].split(",")[0]) * int(x[4:-1].split(",")[1])
                for x in re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
            ]
        )
    print(total)


def b(content: [str]) -> None:
    content = [
        x.split("do()")[1:] if i > 0 else [x]
        for i, x in enumerate("\n".join(content).split("don't()"))
    ]
    content = ["|".join(line_parts) for line_parts in content]

    total = 0
    for line in content:
        total += sum(
            [
                int(x[4:-1].split(",")[0]) * int(x[4:-1].split(",")[1])
                for x in re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
            ]
        )
    print(total)


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
