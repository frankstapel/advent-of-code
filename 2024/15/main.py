import sys


def parse_content(content):
    walls = set()
    boxes = set()
    current = None
    instructions = ""
    for y, line in enumerate(content):
        if line == "":
            continue
        if "#" in line:
            for x, c in enumerate(line):
                if c == "#":
                    walls.add((x, y))
                if c == "O":
                    boxes.add((x, y))
                if c == "@":
                    current = (x, y)
        else:
            instructions += line
    return walls, boxes, current, instructions


def a(content: [str]) -> None:
    walls, boxes, current, instructions = parse_content(content)

    directions = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

    for instruction in instructions:
        next_direction = directions.get(instruction)
        next_position = (current[0] + next_direction[0], current[1] + next_direction[1])
        if next_position in walls:
            continue
        if next_position in boxes:
            next_box_position = next_position
            while True:
                next_box_position = (
                    next_box_position[0] + next_direction[0],
                    next_box_position[1] + next_direction[1],
                )
                if next_box_position in walls:
                    break
                if next_box_position not in boxes:
                    boxes.remove(next_position)
                    boxes.add(next_box_position)
                    current = next_position
                    break
        else:
            current = next_position

    total = 0
    for box in boxes:
        total += box[0] + 100 * box[1]
    print(total)


def parse_content_b(content):
    walls = set()
    boxes = set()
    current = None
    instructions = ""
    for y, line in enumerate(content):
        if line == "":
            continue
        if "#" in line:
            for x, c in enumerate(line):
                if c == "#":
                    walls.add((2 * x, y))
                    walls.add((2 * x + 1, y))
                if c == "O":
                    boxes.add(((2 * x, y), (2 * x + 1, y)))
                if c == "@":
                    current = (2 * x, y)
        else:
            instructions += line
    return walls, boxes, current, instructions


def left(position):
    return (position[0] - 1, position[1])


def right(position):
    return (position[0] + 1, position[1])


def get_boxes(
    boxes,
    left_boxes,
    right_boxes,
    next,
    direction,
    instruction,
    first_call=False,
) -> set:
    affected_boxes = set()
    if instruction == "<" and next in right_boxes:
        left_next = left(next)
        next_box = (left_next, next)
        affected_boxes.add(next_box)
        return affected_boxes.union(
            get_boxes(
                boxes,
                left_boxes,
                right_boxes,
                left(left_next),
                direction,
                instruction,
            )
        )
    if instruction == ">" and next in left_boxes:
        right_next = right(next)
        next_box = (next, right_next)
        affected_boxes.add(next_box)
        return affected_boxes.union(
            get_boxes(
                boxes,
                left_boxes,
                right_boxes,
                right(right_next),
                direction,
                instruction,
            )
        )
    if instruction in "v^":
        box_found = False
        if first_call:
            expansions = [-1, 0]
        else:
            expansions = [-1, 0, 1]
        for expansion in expansions:
            expanded_position = (
                next[0] + expansion,
                next[1],
            )
            expandex_right_position = right(expanded_position)
            expanded_box = (expanded_position, expandex_right_position)
            box_found = True
            if expanded_box in boxes:
                affected_boxes.add(expanded_box)
                affected_boxes = affected_boxes.union(
                    get_boxes(
                        boxes,
                        left_boxes,
                        right_boxes,
                        (
                            expanded_position[0] + direction[0],
                            expanded_position[1] + direction[1],
                        ),
                        direction,
                        instruction,
                    )
                )
        if box_found:
            return affected_boxes
    return set()


def b(content: [str]) -> None:
    walls, boxes, current, instructions = parse_content_b(content)
    left_boxes = {box[0] for box in boxes}
    right_boxes = {box[1] for box in boxes}
    directions = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

    for instruction in instructions:
        direction = directions.get(instruction)
        next = (current[0] + direction[0], current[1] + direction[1])
        if next in walls:
            continue
        if (
            (instruction == ">" and next in left_boxes)
            or (instruction == "<" and next in right_boxes)
            or (instruction in "v^" and (next in left_boxes or next in right_boxes))
        ):
            affected_boxes = get_boxes(
                boxes,
                left_boxes,
                right_boxes,
                next,
                direction,
                instruction,
                True,
            )
            new_boxes = {
                (
                    (box[0][0] + direction[0], box[0][1] + direction[1]),
                    (box[1][0] + direction[0], box[1][1] + direction[1]),
                )
                for box in affected_boxes
            }

            valid = True
            for box in new_boxes:
                if box[0] in walls or box[1] in walls:
                    valid = False
                    break
            if not valid:
                continue

            for box in affected_boxes:
                boxes.remove(box)
            for box in new_boxes:
                boxes.add(box)
            left_boxes = {box[0] for box in boxes}
            right_boxes = {box[1] for box in boxes}
            current = next
        else:
            current = next

    total = 0
    for box in boxes:
        left_box = box[0]
        total += left_box[0] + 100 * left_box[1]
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
