import sys


def a(content: [str]) -> None:
    correct_results = []

    for line in content:
        answer, inputs = line.split(": ")
        answer = int(answer)
        inputs = [int(x) for x in inputs.split(" ")]

        current_values = set()
        current_values.add(inputs[0])

        for input in inputs[1:]:
            new_values = set()
            for value in current_values:
                new_values.add(value + input)
                new_values.add(value * input)
            current_values = new_values

        if answer in current_values:
            correct_results.append(answer)

    print(sum(correct_results))


def b(content: [str]) -> None:
    correct_results = []

    for line in content:
        answer, inputs = line.split(": ")
        answer = int(answer)
        inputs = [int(x) for x in inputs.split(" ")]

        current_values = set()
        current_values.add(inputs[0])

        for input in inputs[1:]:
            new_values = set()
            for value in current_values:
                new_values.add(value + input)
                new_values.add(value * input)
                new_values.add(int(str(value) + str(input)))
            current_values = new_values

        if answer in current_values:
            correct_results.append(answer)

    print(sum(correct_results))


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
