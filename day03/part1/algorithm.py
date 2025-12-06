from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def joltage(input_data=None):
    if input_data is None: return 0
    joltage_total = 0
    for row in input_data:
        batteries = list(map(int, row))
        battery_one = max(batteries[:-1])
        max_index = batteries.index(battery_one) 
        battery_two = max(batteries[max_index + 1:])
        joltage_total += battery_one * 10 + battery_two
    return joltage_total

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("First 5:", input_data[:5])
    print("Total Joltage:", joltage(input_data))
