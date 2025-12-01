from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def zerocount(input_data=None):
    if input_data is None: return 0
    zeros = 0
    count = 50
    for row in input_data:
        direction = 1 if row[0] == 'R' else -1
        num = int(row[1:])
        count += direction * num
        if count % 100 == 0:
            zeros += 1
    return zeros

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data.txt")
    print("First 5:", input_data[:5])
    print("Zerocount:", zerocount(input_data))
