import numpy as np
from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

pass_array = np.zeros((10, 10), dtype=int)

for i, row in enumerate(input_data):
    for j, char in enumerate(row):
        pass_array[i, j] = 1


def toilet_checker(grid):
    # make it all one line
    w = 10
    h = 10
    length = len(grid)
    count_array = np.zeros((h + 2, w + 2), dtype=int)
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == '@':
                count_array[i, j] += 1
                count_array[i, j + 1] += 1
                count_array[i, j + 2] += 1
                count_array[i + 1, j] += 1
                count_array[i + 1, j + 2] += 1
                count_array[i + 2, j] += 1
                count_array[i + 2, j + 1] += 1
                count_array[i + 2, j + 2] += 1
    
    total_count = 0
    
    for i, x, y in enumerate(zip(grid, count_array[1: -1])):
        for c, d in zip(x, y[1: -1]):
            if c == '@' and d < 4:
                total_count += 1
    
    if not total_count:
        return 0
    
    return total_count + toilet_checker(pass_array)

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("First 5:", input_data[:5])
    print("Accessible Rolls:", toilet_checker(pass_array))

    # loop thropugh count array from start and end index to check
    # also got to check if position is toilet roll