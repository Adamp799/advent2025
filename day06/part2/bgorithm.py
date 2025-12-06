from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip('\n') for line in f if line.strip()]
    except FileNotFoundError:
        return []


def sum_of_problems(problems):
    print(problems)
    #operations = problems[-1]
    #operation = operations.strip()
    #print(operation)
    #or i in range(len(problems[0])):
        #or j in problems:
    total = 0
    return total


if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {input_data} from data")
    print("Grand Total:", sum_of_problems(input_data))