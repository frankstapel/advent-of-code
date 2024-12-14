import sys
from functools import cache
from tqdm import tqdm


def parse_line(line) -> (int, int, int, int):
    p, v = line.split(" ")
    p = p[2:].split(",")
    v = v[2:].split(",")
    px, py = int(p[0]), int(p[1])
    vx, vy = int(v[0]), int(v[1])
    return px, py, vx, vy


@cache
def get_quadrant(px, py, max_x, max_y) -> int:
    half_x = max_x // 2
    half_y = max_y // 2
    if px < half_x and py < half_y:
        return 0
    elif px > half_x and py < half_y:
        return 1
    elif px < half_x and py > half_y:
        return 2
    elif px > half_x and py > half_y:
        return 3


def a(content: [str]) -> None:
    quadrants = {i: 0 for i in range(4)}
    max_x = 101
    max_y = 103
    # max_x = 11
    # max_y = 7
    seconds = 100
    for line in content:
        px, py, vx, vy = parse_line(line)
        px = (px + vx * seconds) % max_x
        py = (py + vy * seconds) % max_y
        quadrant = get_quadrant(px, py, max_x, max_y)
        if quadrant in quadrants:
            quadrants[quadrant] += 1
    safety_factor = 1
    for robots in quadrants.values():
        safety_factor *= robots
    print(quadrants)
    print(safety_factor)


def visualize(grid, seconds) -> None:
    # append the visualisation to output.txt
    with open("output.txt", "a") as f:
        f.write(f"Seconds: {seconds}\n")
        for y in range(103):
            for x in range(101):
                if grid[(x, y)] > 0:
                    f.write("#")
                else:
                    f.write(".")
            f.write("\n")
        f.write("\n")


def b(content: [str]) -> None:
    max_x = 101
    max_y = 103
    lines = [parse_line(line) for line in content]
    for seconds in tqdm(range(1000000)):
        if ((seconds - 28) % max_y == 0) and ((seconds - 55) % max_x == 0):
            pass
        else:
            continue
        grid = {}
        for x in range(max_x):
            for y in range(max_y):
                grid[(x, y)] = 0
        for px, py, vx, vy in lines:
            px = (px + vx * seconds) % max_x
            py = (py + vy * seconds) % max_y
            grid[(px, py)] += 1
        visualize(grid, seconds)


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
