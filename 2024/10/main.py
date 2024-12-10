import sys


def a(content: [str]) -> None:
    grid = {}
    neighbor_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            grid[(x, y)] = {"value": int(c), "low_neighbors": [], "nines": set()}

    queue = set()
    for (x, y), v in grid.items():
        value = v["value"]
        if value == 9:
            queue.add((x, y))
        for neighbor_delta in neighbor_deltas:
            neighbor_coord = (x + neighbor_delta[0], y + neighbor_delta[1])
            neighbor_value = grid.get(neighbor_coord, {}).get("value")
            if neighbor_coord in grid and neighbor_value == value - 1:
                grid[(x, y)]["low_neighbors"].append(neighbor_coord)
                if value == 9:
                    grid[neighbor_coord]["nines"].add((x, y))

    trailheads = set()
    while queue:
        new_queue = set()
        for x, y in queue:
            current = grid[(x, y)]
            for neighbor_coords in current["low_neighbors"]:
                neighbor = grid[neighbor_coords]
                neighbor["nines"].update(current["nines"])
                if neighbor["value"] > 0:
                    new_queue.add(neighbor_coords)
                else:
                    trailheads.add(neighbor_coords)
        queue = new_queue

    print(sum(len(grid[trailhead]["nines"]) for trailhead in trailheads))


def b(content: [str]) -> None:
    grid = {}
    neighbor_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            grid[(x, y)] = {"value": int(c), "low_neighbors": [], "nine_paths": set()}

    queue = set()
    for (x, y), v in grid.items():
        value = v["value"]
        if value == 9:
            queue.add((x, y))
        for neighbor_delta in neighbor_deltas:
            neighbor_coord = (x + neighbor_delta[0], y + neighbor_delta[1])
            neighbor_value = grid.get(neighbor_coord, {}).get("value")
            if neighbor_coord in grid and neighbor_value == value - 1:
                grid[(x, y)]["low_neighbors"].append(neighbor_coord)
                if value == 9:
                    grid[neighbor_coord]["nine_paths"].add(((x, y)))

    trailheads = set()
    while queue:
        new_queue = set()
        for x, y in queue:
            current = grid[(x, y)]
            for neighbor_coords in current["low_neighbors"]:
                neighbor = grid[neighbor_coords]
                for nine_path in current["nine_paths"]:
                    neighbor["nine_paths"].add(((x, y), *nine_path))
                if neighbor["value"] > 0:
                    new_queue.add(neighbor_coords)
                else:
                    trailheads.add(neighbor_coords)
        queue = new_queue

    print(sum(len(grid[trailhead]["nine_paths"]) for trailhead in trailheads))


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
