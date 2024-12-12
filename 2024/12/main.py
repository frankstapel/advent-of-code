import sys


def a(content: [str]) -> None:
    grid = {}
    unprocessed = set()
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            unprocessed.add((x, y))
    neighbor_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    total_count = 0
    while unprocessed:
        current_region = unprocessed.pop()
        current_fence_count = 0
        current_plot_count = 0
        queue = set()
        queue.add(current_region)
        while queue:
            current = queue.pop()
            current_plot_count += 1
            current_value = grid.get(current)
            for delta in neighbor_deltas:
                neighbor = (current[0] + delta[0], current[1] + delta[1])
                if grid.get(neighbor) == current_value and neighbor in unprocessed:
                    queue.add(neighbor)
                    unprocessed.discard(neighbor)
                elif grid.get(neighbor) != current_value:
                    current_fence_count += 1
        total_count += current_fence_count * current_plot_count
    print(total_count)


def same_direction(n1, n2, n3) -> bool:
    return (n2[1] - n1[1]) * (n3[0] - n2[0]) == (n3[1] - n2[1]) * (n2[0] - n1[0])


def get_left_node(edge, grid) -> str:
    n1, n2 = edge
    if n1[0] == n2[0]:
        # Horizontal
        if n1[1] > n2[1]:
            # Left
            return grid.get((n2[0], n2[1] - 1))
        else:
            # Right
            return grid.get(n1)
    else:
        # Vertical
        if n1[0] > n2[0]:
            # Down
            return grid.get(n2)
        else:
            # Up
            return grid.get((n1[0] - 1, n1[1]))


def b(content: [str]) -> None:
    grid = {}
    unprocessed = set()
    for y, line in enumerate(content[::-1]):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            unprocessed.add((x, y))

    regions = {}
    neighbor_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    region_id = 0
    while unprocessed:
        current_region = unprocessed.pop()
        region = {"nodes": set()}
        queue = set()
        queue.add(current_region)
        while queue:
            current = queue.pop()
            region["nodes"].add(current)
            current_value = grid.get(current)
            for delta in neighbor_deltas:
                neighbor = (current[0] + delta[0], current[1] + delta[1])
                if grid.get(neighbor) == current_value and neighbor in unprocessed:
                    queue.add(neighbor)
                    unprocessed.discard(neighbor)
        region["value"] = current_value
        region_id += 1
        regions[region_id] = region

    neighbor_edges = {
        (0, 1): ((0, 1), (1, 1)),
        (1, 0): ((1, 0), (1, 1)),
        (0, -1): ((0, 0), (1, 0)),
        (-1, 0): ((0, 0), (0, 1)),
    }
    neighbor_order = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    total_count = 0
    for region_id, region in regions.items():
        current_plot_count = len(region["nodes"])
        edges = set()
        for n1, n2 in region["nodes"]:
            for (nd1, nd2), ((e11, e12), (e21, e22)) in neighbor_edges.items():
                neighbor = (n1 + nd1, n2 + nd2)
                if grid.get(neighbor) != region["value"]:
                    edges.add(((n1 + e11, n2 + e12), (n1 + e21, n2 + e22)))

        all_nodes = []
        while edges:
            nodes = list(edges.pop())
            if get_left_node(nodes, grid) != region["value"]:
                nodes = nodes[::-1]
            while nodes[0] != nodes[-1]:
                # Check the possible next edges clockwise
                current_direction = (
                    nodes[-1][0] - nodes[-2][0],
                    nodes[-1][1] - nodes[-2][1],
                )
                current_index = neighbor_order.index(current_direction)
                for i in range(4):
                    next_direction = neighbor_order[
                        (current_index + i + 2) % 4
                    ]  # + 2 to circle clockwise from the backwards direction
                    print(next_direction)
                    next_node = (
                        nodes[-1][0] + next_direction[0],
                        nodes[-1][1] + next_direction[1],
                    )
                    if (nodes[-1], next_node) in edges or (
                        next_node,
                        nodes[-1],
                    ) in edges:
                        nodes.append(next_node)
                        edges.discard((nodes[-2], next_node))
                        edges.discard((next_node, nodes[-2]))
                        break
            all_nodes.append(nodes)

        current_fence_count = 0
        for nodes in all_nodes:
            nodes.append(nodes[1])
            nodes.append(nodes[2])
            for i in range(len(nodes) - 3):
                if not same_direction(nodes[i], nodes[i + 1], nodes[i + 2]):
                    current_fence_count += 1
        total_count += current_fence_count * current_plot_count
    print(total_count)


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
