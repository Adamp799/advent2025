from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            raw_lines = [line.rstrip("\n") for line in f]
            idx = raw_lines.index("") 
            return [raw_lines[:idx], raw_lines[idx+1:]]
        return None
    except FileNotFoundError:
        return []

def total_fresh(ranges):
    fresh_set = set()
    for i in ranges:
        x = i.split('-')
        fresh_set = fresh_set.union(set(range(int(x[0]), int(x[1]) + 1)))
    return len(fresh_set)

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {input_data[0][:5]} from data")
    print("Possible Fresh Ingredients:", total_fresh(input_data[0]))
