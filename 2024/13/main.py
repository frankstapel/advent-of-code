import sys
from tqdm import tqdm
from functools import cache
import numpy as np


def retrieve_problems(content: [str]) -> [dict]:
    problems = []
    problem = {}
    for line in content:
        if line.startswith("Button A: "):
            problem["button_a"] = retrieve_x_y(line)
        elif line.startswith("Button B: "):
            problem["button_b"] = retrieve_x_y(line)
        elif line.startswith("Prize: "):
            line = line.split(": ")[1]
            x_prize, y_prize = line.split(", ")
            x_prize = x_prize[2:]
            y_prize = y_prize[2:]
            problem["prize"] = (int(x_prize), int(y_prize))
        else:
            problems.append(problem)
            problem = {}
    problems.append(problem)
    return problems


def retrieve_x_y(line: str) -> (int, int):
    content = line.split(": ")[1]
    x, y = content.split(", ")
    x = x[2:]
    y = y[2:]
    return int(x), int(y)


@cache
def token_cost(button_a, button_b, remaining_prize, a_presses, b_presses) -> int:
    # Check if the prize is already at the right spot
    if remaining_prize == (0, 0):
        return 0

    # Check if the prize is negative
    if remaining_prize[0] < 0 or remaining_prize[1] < 0:
        return float("inf")

    # Check if the maximum depth has been reached
    if a_presses > 100 or b_presses > 100:
        return float("inf")

    # Try pressing each button, return the cost of the cheapest path
    cost_a = 3
    cost_b = 1

    x_a, y_a = button_a
    x_b, y_b = button_b
    x_prize, y_prize = remaining_prize
    total_cost_a = cost_a + token_cost(
        button_a, button_b, (x_prize - x_a, y_prize - y_a), a_presses + 1, b_presses
    )
    total_cost_b = cost_b + token_cost(
        button_a, button_b, (x_prize - x_b, y_prize - y_b), a_presses, b_presses + 1
    )
    return min(total_cost_a, total_cost_b)


def a(content: [str]) -> None:
    problems = retrieve_problems(content)

    total_cost = 0
    for problem in tqdm(problems):
        problem_token_cost = token_cost(
            problem["button_a"], problem["button_b"], problem["prize"], 0, 0
        )
        if problem_token_cost != float("inf"):
            total_cost += problem_token_cost
    print(total_cost)


def b(content: [str]) -> None:
    problems = retrieve_problems(content)

    cost_a = 3
    cost_b = 1
    prize_increase = 10000000000000
    accepted_error = 1e-4
    total_cost = 0
    for problem in problems:
        x_a, y_a = problem["button_a"]
        x_b, y_b = problem["button_b"]
        x_prize, y_prize = problem["prize"]

        A = np.array([[x_a, x_b], [y_a, y_b]])
        b = np.array([x_prize + prize_increase, y_prize + prize_increase])
        # Numpy can hopefully solve Ax = b. THANK YOU NUMPY!!!
        a_presses, b_presses = np.linalg.solve(A, b)

        # Leave room for floating point errors
        if (
            abs(a_presses - round(a_presses)) < accepted_error
            and abs(b_presses - round(b_presses)) < accepted_error
        ):
            total_cost += cost_a * round(a_presses) + cost_b * round(b_presses)

    print(total_cost)


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
