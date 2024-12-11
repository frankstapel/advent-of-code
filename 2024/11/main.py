import sys
from functools import cache


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


def a(content: [str]) -> None:
    content = map(int, content[0].split(" "))
    head = None
    prev = None
    number_of_nodes = 0

    for value in content:
        node = Node(value)
        number_of_nodes += 1
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
        prev = node

    for i in range(25):
        print(i, number_of_nodes)
        current = head
        while current:
            # str_value = str(current.value)
            if current.value == 0:
                current.value = 1
            elif len(str_value := str(current.value)) % 2 == 0:
                # print(str_value)
                half = len(str_value) // 2
                first = int(str_value[:half])
                second = int(str_value[half:])
                current.value = first
                new_node = Node(second)
                number_of_nodes += 1
                new_node.next = current.next
                current.next = new_node
                current = new_node
            else:
                current.value *= 2024
            current = current.next

    print(number_of_nodes)


@cache
def dive(value: int, depth: int) -> int:
    if depth == 75:
        return 1

    next_depth = depth + 1
    if value == 0:
        return dive(1, next_depth)
    elif len(str_value := str(value)) % 2 == 0:
        half = len(str_value) // 2
        first = int(str_value[:half])
        second = int(str_value[half:])
        return dive(first, next_depth) + dive(second, next_depth)
    else:
        return dive(value * 2024, next_depth)


def b(content: [str]) -> None:
    content = map(int, content[0].split(" "))
    number_of_nodes = 0
    for i in content:
        number_of_nodes += dive(i, 0)
    print(number_of_nodes)


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
