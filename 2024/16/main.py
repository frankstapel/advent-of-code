import sys
from queue import PriorityQueue


def a(content: [str]) -> None:
    grid = {}
    priority_queue = PriorityQueue()
    end = None
    directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            if c == "#":
                continue
            for direction in directions:
                if c == "S" and direction == 1:
                    grid[(x, y, direction)] = 0
                    priority_queue.put((0, (x, y, direction)))
                else:
                    grid[(x, y, direction)] = float("inf")
            if c == "E":
                end = (x, y)
    while not priority_queue.empty():
        cost, (x, y, direction) = priority_queue.get()
        if (x, y) == end:
            break
        for i in range(3):
            new_direction = (direction + i - 1) % 4
            delta = directions[new_direction]
            if i == 1:
                new_position = (x + delta[0], y + delta[1], new_direction)
                new_cost = cost + 1
            else:
                new_position = (x, y, new_direction)
                new_cost = cost + 1000
            if new_position in grid and new_cost < grid[new_position]:
                grid[new_position] = new_cost
                priority_queue.put((new_cost, new_position))


def b(content: [str]) -> None:
    grid = {}
    priority_queue = PriorityQueue()
    end = None
    directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            if c == "#":
                continue
            for direction in directions:
                if c == "S" and direction == 1:
                    grid[(x, y, direction)] = {"cost": 0, "visited": {(x, y)}}
                    priority_queue.put((0, (x, y, direction)))
                else:
                    grid[(x, y, direction)] = {
                        "cost": float("inf"),
                        "visited": {(x, y)},
                    }
            if c == "E":
                end = (x, y)
    winning_nodes = set()
    while not priority_queue.empty():
        cost, (x, y, direction) = priority_queue.get()
        if (x, y) == end:
            winning_nodes.update(grid[(x, y, direction)]["visited"])
            break
        for i in range(3):
            new_direction = (direction + i - 1) % 4
            delta = directions[new_direction]
            if i == 1:
                new_position = (x + delta[0], y + delta[1], new_direction)
                new_cost = cost + 1
            else:
                new_position = (x, y, new_direction)
                new_cost = cost + 1000
            if new_position in grid and new_cost <= grid[new_position]["cost"]:
                grid[new_position]["cost"] = new_cost
                grid[new_position]["visited"].update(grid[(x, y, direction)]["visited"])
                priority_queue.put((new_cost, new_position))
    print(len(winning_nodes))


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
