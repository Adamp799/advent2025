from pathlib import Path
import numpy as np
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def tachyon_beam(input_data):
    # make it all one line
    w = len(input_data[0]) + 2
    h = len(input_data) + 2
    beam_location = input_data[0].index('S')
    count_array = np.zeros((h + 2, w + 2), dtype=int)
    count_array[0, beam_location] = 1
    for i, row in enumerate(input_data[1:]):
        for j, char in enumerate(row):
            if char == '^':
                count_array[i + 1, j + 1] = 0
            else:
                count_array[i + 1, j + 1] += count_array[i, j + 1]
                if row[j - 1] == '^':
                    count_array[i + 1, j + 1] += count_array[i, j]
                if row[j + 1] == '^':
                    count_array[i + 1, j + 1] += count_array[i, j + 2]
    print(count_array)
    return(sum(count_array[-1]))

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Total Splits:", tachyon_beam(input_data))
