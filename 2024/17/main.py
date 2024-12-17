import sys
from tqdm import tqdm


def parse_content(content: [str]) -> [str]:
    a = int(content[0].split(": ")[1])
    b = int(content[1].split(": ")[1])
    c = int(content[2].split(": ")[1])
    instructions = [int(i) for i in content[4].split(": ")[1].split(",")]
    return a, b, c, instructions


def execute(instructions: [int], a: int, b: int, c: int) -> int:
    ip = 0
    output = []
    while ip <= len(instructions) - 1:
        instruction = instructions[ip]
        combo = literal = instructions[ip + 1]
        if combo == 4:
            combo = a
        elif combo == 5:
            combo = b
        elif combo == 6:
            combo = c

        jumped = False
        if instruction == 0:
            # adv -> A = A DIV (2 ** COMBO OP)
            a = a // (2**combo)
        elif instruction == 1:
            # bxl -> B = B XOR LITERAL OP
            b = b ^ literal
        elif instruction == 2:
            # bst -> B = COMBO OP MOD 8
            b = combo % 8
        elif instruction == 3:
            # jnz -> JMP to LITERAL OP
            if a != 0:
                ip = literal
                jumped = True
        elif instruction == 4:
            # bxc -> B XOR C
            b = b ^ c
        elif instruction == 5:
            # out -> OUTPUT COMBO OP MOD 8
            output.append(str(combo % 8))
        elif instruction == 6:
            # bdv -> B = A DIV (2 ** COMBO OP)
            b = a // (2**combo)
        elif instruction == 7:
            # cdv -> C = A DIV (2 ** COMBO OP)
            c = a // (2**combo)

        if not jumped:
            ip += 2

    return ",".join(output)


def a(content: [str]) -> None:
    a, b, c, instructions = parse_content(content)
    print(execute(instructions, a, b, c))


def execute_faster(a, b, c):
    result = []
    while a > 0:
        b = a % 8 ^ 1
        c = a // 2**b
        b = b ^ 5 ^ c
        result.append(b % 8)
        a = a // 8
    return result


def b(content: [str]) -> None:
    # Solved with a hint, not counting this one towards leaderboard.
    _, _, _, instructions = parse_content(content)
    queue = [0]
    while queue:
        a = queue.pop(0)
        for i in range(8):
            next_a = (a << 3) + i
            result = execute_faster(next_a, 0, 0)
            if result == instructions[-len(result):]:
                queue.append(next_a)
                if result == instructions:
                    print(next_a)
                    return


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
