from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def tachyon_beam(input_data):
    total_splits = 0
    beam_locations = set()
    beam_locations.add(input_data[0].index('S'))
    for line in input_data[1:]:
        splitters = {i for i, char in enumerate(line) if char == '^'}
        intersections = beam_locations.intersection(splitters)
        total_splits += len(intersections)
        beam_locations.update({y for x in intersections for y in (x - 1, x + 1) if 0 <= y <= len(line) - 1})
        beam_locations.difference_update(intersections)
    return total_splits

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Total Splits:", tachyon_beam(input_data))
