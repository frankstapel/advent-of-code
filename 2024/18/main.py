import sys
from queue import PriorityQueue


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(start, finish, available_nodes):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_scores = {start: 0}
    f_scores = {start: manhattan_distance(start, finish)}
    neighbor_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while not open_set.empty():
        current = open_set.get()[1]

        if current == finish:
            break

        for dx, dy in neighbor_deltas:
            neighbor = (current[0] + dx, current[1] + dy)
            if neighbor not in available_nodes:
                continue

            tentative_g_score = g_scores[current] + 1
            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + manhattan_distance(
                    neighbor, finish
                )
                open_set.put((f_scores[neighbor], neighbor))

    current = finish
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def a(content: [str]) -> None:
    available_nodes = set()
    start = (0, 0)
    finish = (70, 70)
    for x in range(71):
        for y in range(71):
            available_nodes.add((x, y))
    for index, line in enumerate(content):
        if index == 1024:
            break
        x, y = map(int, line.split(","))
        available_nodes.discard((x, y))

    path = a_star(start, finish, available_nodes)
    print(path)
    print(len(path) - 1)


def b(content: [str]) -> None:
    available_nodes = set()
    start = (0, 0)
    finish = (70, 70)
    for x in range(71):
        for y in range(71):
            available_nodes.add((x, y))
    for index, line in enumerate(content):
        x, y = map(int, line.split(","))
        available_nodes.discard((x, y))

        if index < 1024:
            continue

        path = a_star(start, finish, available_nodes)
        if len(path) - 1 == 0:
            print(f"{x},{y}")
            break


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
