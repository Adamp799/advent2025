from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            raw_lines = [line.rstrip("\n") for line in f]
            idx = raw_lines.index("") 
            return [raw_lines[:idx], raw_lines[idx+1:]]
        return None
    except FileNotFoundError:
        return []

def total_fresh(merged_ranges):
    count = 0
    for i in merged_ranges: 
        count += (i[1] - i[0] + 1)
    return count

def merge_ranges(ranges):
    parsed = []
    for r in ranges:
        parts = r.strip().split("-")
        start, end = int(parts[0]), int(parts[1])
        parsed.append([start, end])

    parsed.sort(key=lambda x: x[0])
    merged = []
    for start, end in parsed:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return [tuple(r) for r in merged]

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {input_data[0][:5]} from data")
    merged_ranges = merge_ranges(input_data[0])
    print("Possible Fresh Ingredients:", total_fresh(merged_ranges))
