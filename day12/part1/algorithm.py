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
    valid_regions = 0
    regions = input_data[-1]; presents = input_data[:-1]; present_sizes = []
    for i in range(0, len(presents)):
        present_sizes.append(sum(line.count("#") for line in presents[i][1:]))
    
    for region in regions: 
        components = region.split(" ")
        [x, y] = map(int, components[0].strip(':').split("x"))
        area = x * y; three_by_three_area = (x // 3) * (y // 3)
        present_counts = [int(i) for i in components[1:]]

        required_area = 0
        for i, c in enumerate(present_counts): 
            required_area += present_sizes[i] * c
        
        if required_area > area: continue
        if len(presents) <= three_by_three_area: valid_regions += 1; continue
        
    return valid_regions
   
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} nodes from data")
    print("Number of Valid Regions:", validate_regions(input_data))
