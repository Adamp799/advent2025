from pathlib import Path
from itertools import groupby
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            lines = [line.rstrip('\n') for line in f]
            return [list(group) for key, group in groupby(lines, key=lambda x: x == "") if not key]
    except FileNotFoundError:
        return []

def validate_regions(input_data):
    regions = input_data[-1]
    presents = input_data[:-1]
    for region in regions: 
        components = region.split(" ")
        [x, y] = map(int, components[0].strip(':').split("x"))
        present_indices = [int(i) for i in components[1:]]
        for i in present_indices: 
            print(presents[i])
   
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} nodes from data")
    print("Number of Valid Regions:", validate_regions(input_data))
