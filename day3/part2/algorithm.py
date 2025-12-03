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
        joltage = recursive_battery_search(batteries)
        joltage_total += joltage
    return joltage_total

def recursive_battery_search(batteries=None, depth=0):
    if batteries is None or len(batteries) == 0: return 0
    if depth >= 12: return 0
    joltage_options = []
    for i in range(len(batteries)):
        joltage_options.append(batteries[i] * 10 ** (11 - depth) + recursive_battery_search(batteries[i+1:], depth + 1))
    cleaned_joltage_options = [int(str(joltage).replace("0", "")) for joltage in joltage_options]
    return max(cleaned_joltage_options) if cleaned_joltage_options else 0

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("First 5:", input_data[:5])
    print("Total Joltage:", joltage(input_data))
