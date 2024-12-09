import sys


def a(content: [str]) -> None:
    disk_map = [int(x) for x in content[0]]
    blocks = []
    empty_indexes = []
    current_block_id = 0
    current_block_index = 0

    for disk_index, disk in enumerate(disk_map):
        if disk_index % 2 == 0:
            for _ in range(disk):
                blocks.append(current_block_id)
                current_block_index += 1
            current_block_id += 1
        else:
            for _ in range(disk):
                empty_indexes.append(current_block_index)
                blocks.append(None)
                current_block_index += 1

    for i in range(len(blocks) - 1, 0, -1):
        if empty_indexes[0] >= i:
            break

        if blocks[i] is None:
            continue
        else:
            next_empty_index = empty_indexes.pop(0)
            blocks[next_empty_index] = blocks[i]
            blocks[i] = None
    print(sum(index * id for index, id in enumerate(blocks) if id))


def b(content: [str]) -> None:
    disk_map = [int(x) for x in content[0]]
    blocks = []
    empty_spaces = []
    current_block_id = 0
    current_block_index = 0

    for disk_index, disk in enumerate(disk_map):
        if disk_index % 2 == 0:
            blocks.append((current_block_index, disk, current_block_id))
            current_block_id += 1
        elif disk > 0:
            empty_spaces.append((current_block_index, disk))
        current_block_index += disk

    final_blocks = []

    for block in blocks[::-1]:
        block_index, block_length, block_id = block
        block_moved = False
        for empty_space in empty_spaces:
            empty_index, empty_length = empty_space
            if block_index > empty_index and block_length <= empty_length:
                final_blocks.append((empty_index, block_length, block_id))
                empty_spaces.remove(empty_space)
                if block_length < empty_length:
                    empty_spaces.append(
                        (empty_index + block_length, empty_length - block_length)
                    )
                    empty_spaces = sorted(empty_spaces, key=lambda x: x[0])
                block_moved = True
                break
        if not block_moved:
            final_blocks.append((block[0], block[1], block[2]))

    check_sum = 0
    for index, length, id in final_blocks:
        for i in range(length):
            check_sum += (index + i) * id
    print(check_sum)


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
