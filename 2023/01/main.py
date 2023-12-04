def parse_input():
    # Define the file's name.
    filename = "input.txt"

    # Open the file and read its content.
    with open(filename) as f:
        content = f.read().splitlines()

    return content


def a():
    input = parse_input()
    # print(input)
    final_counts = []
    for i in input:
        result = ""
        # print(i)
        for j in i:
            if j.isdigit():
                result += j
                break
        i = i[::-1]
        # print(i)
        for j in i:
            if j.isdigit():
                result += j
                break
        # print(result)
        final_counts.append(int(result))

    print(sum(final_counts))


def b():
    input = parse_input()

    replacements = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    reversed_replacements = {}
    for characters, number in replacements.items():
        reversed_replacements[characters[::-1]] = number

    final_counts = []
    for i in input:
        result = ""
        first_found = False
        second_found = False
        while not second_found:
            if not first_found:
                replacement_found = False
                if i[0].isdigit():
                    result += i[0]
                    # i = i[1:]
                    first_found = True
                    i = i[::-1]
                    replacement_found = True
                else:
                    # Try to match the characters wiht the first occurence
                    for (characters, number) in replacements.items():
                        if i.startswith(characters):
                            result += number
                            # i = i[len(characters):]
                            first_found = True
                            i = i[::-1]
                            replacement_found = True
                            break
                if not replacement_found:
                    # maybe build in reverse checks?
                    i = i[1:]
            else:
                # print(i)
                replacement_found = False
                if i[0].isdigit():
                    result += i[0]
                    second_found = True
                    replacement_found = True
                else:
                    # Try to match the characters wiht the first occurence
                    for (characters, number) in reversed_replacements.items():
                        if i.startswith(characters):
                            result += number
                            second_found = True
                            replacement_found = True
                            break
                if not replacement_found:
                    # maybe build in reverse checks?
                    i = i[1:]
        final_counts.append(int(result))

    print(sum(final_counts))


if __name__ == "__main__":
    a()
    b()
