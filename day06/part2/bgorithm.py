from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip('\n') for line in f if line.strip()]
    except FileNotFoundError:
        return []


def sum_of_problems(problems):
    operations = problems[-1]
    operation = operations[0]
    total = 0
    prod = 1
    print(operation)

    for i in range(len(problems[0])):
        if operations[i] == '+' and i > 0:
            total += prod
            prod = 1
            operation = '+'
        elif operations[i] == '*' and i > 0:
            total += prod
            prod = 1
            operation = '*'
        
        build = 0
        full = 0

        for j in range(4):
            if not problems[j][i] == ' ':
                full += 1
                build = build*10 + int(problems[j][i])
        
        if operation == '+':
            total += build
        elif full:
            prod *= build
    
    print(total)


    if operation == '*' and build:
        total += prod
    
    
    return total - operations.count('+') + 1


if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {input_data} from data")
    print("Grand Total:", sum_of_problems(input_data))