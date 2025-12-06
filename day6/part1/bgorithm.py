from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def sum_of_problems(problems):
    total = 0

    for problem in problems:
        nums = [int(num) for num in problem[:-1]]
        operation = problem[-1]

        if operation == '+':
            total += sum(nums)
        else:
            product = 1
            for num in nums:
                product *= num
            total += product
    
    return total