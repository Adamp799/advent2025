from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def tachyon_beam(input_data):
    beam_locations = set()
    beam_locations.add(input_data[0].index('S'))
    for line in input_data[1:]:
        splitters = {i for i, char in enumerate(line) if char == '^'}

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print(input_data)
    print("Total Splits:", tachyon_beam(input_data))
