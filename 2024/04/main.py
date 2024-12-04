import sys
import re


def rotate_90(matrix):
    return list(zip(*matrix[::-1]))


def rotate_45(matrix):
    new_matrix = []
    for x in range(2 * len(matrix) - 1):
        new_matrix.append(
            [matrix[y][x - y] for y in range(len(matrix)) if 0 <= x - y < len(matrix)]
        )
    return new_matrix


def visualize(matrix):
    for row in matrix:
        print("".join(row))
    print("")


def a(content: [str]) -> None:
    content = [[c for c in line] for line in content]
    all_angles = []
    for _ in range(4):
        content = rotate_90(content)
        all_angles.append(content.copy())
        all_angles.append(rotate_45(content).copy())

    occurences = 0
    for angle in all_angles:
        for line in angle:
            occurences += len(re.findall(r"XMAS", "".join(line)))

    print(occurences)


def b(content: [str]) -> None:
    content = [[c for c in line] for line in content]
    occurences = 0
    for x in range(len(content) - 2):
        for y in range(len(content[x]) - 2):
            diagonal_1 = "".join(
                [content[x][y], content[x + 1][y + 1], content[x + 2][y + 2]]
            )
            diagonal_2 = "".join(
                [content[x][y + 2], content[x + 1][y + 1], content[x + 2][y]]
            )
            if (diagonal_1 == "MAS" or diagonal_1 == "SAM") and (
                diagonal_2 == "MAS" or diagonal_2 == "SAM"
            ):
                occurences += 1
    print(occurences)


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
