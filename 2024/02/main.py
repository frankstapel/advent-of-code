import sys


def a(content: [str]) -> None:
    safe_reports = 0
    for report in content:
        report = report.split(" ")
        safe = True
        increasing = False
        for index, level in enumerate(report):
            current = int(level)
            previous = int(report[index - 1])
            if index == 0:
                continue

            if index == 1 and current > previous:
                increasing = True

            if current < previous and increasing:
                safe = False

            if current > previous and not increasing:
                safe = False

            if abs(current - previous) > 3 or abs(current - previous) < 1:
                safe = False

        if safe:
            safe_reports += 1
        print(safe_reports)


def b(content: [str]) -> None:
    safe_reports = 0
    for report in content:
        report = report.split(" ")
        options = [report]
        for i in range(len(report)):
            report_copy: [str] = report.copy()
            del report_copy[i]
            options.append(report_copy)

        safe_option_found = False
        for option in options:
            safe = True
            increasing = False
            for index, level in enumerate(option):
                current = int(level)
                previous = int(option[index - 1])
                if index == 0:
                    continue

                if index == 1 and current > previous:
                    increasing = True

                if current < previous and increasing:
                    safe = False

                if current > previous and not increasing:
                    safe = False

                if abs(current - previous) > 3 or abs(current - previous) < 1:
                    safe = False

            if safe:
                safe_option_found = True
                break
        if safe_option_found:
            safe_reports += 1
    print(safe_reports)


############################
### Start of boilerplate ###
############################

def parse_input(filename) -> [str]:
    with open(filename) as f:
        content = f.read().splitlines()
    return content


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Please pass a puzzle part as argument')

    if len(sys.argv) > 2 and sys.argv[2].lower() in ['test', '-t', 't']:
        filename = f'test_{sys.argv[1].lower()}.txt'
    else:
        filename = 'input.txt'
    content = parse_input(filename)

    print(f'\nTesting part {sys.argv[1].upper()} on {filename}\n')

    if sys.argv[1].lower() == 'a':
        a(content)
    elif sys.argv[1].lower() == 'b':
        b(content)

    print('')
