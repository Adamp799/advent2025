from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            lines = [line.strip().split() for line in f if line.strip()]
            return lines
    except FileNotFoundError:
        return []

def sum_of_problems(problems):
    total = 0

    for i in range(len(problems[0])):
        operation = problems[-1][i]
        if operation == '+':
            count = 0
            for problem in problems[:-1]:
                count += int(problem[i])
            total += count
        else:
            prod = 1
            for problem in problems[:-1]:
                prod *= int(problem[i])
            total += prod
    return total


if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {input_data} from data")
    print("Grand Total:", sum_of_problems(input_data))