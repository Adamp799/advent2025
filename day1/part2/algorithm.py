from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

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
        if row[0] == 'R':
            direction = 1
        else:
            direction = -1
        num = int(row[1:])
        quot = num // 100
        zeros += quot

        # check if we go past zero
        if direction and num % 100 >= 100 - count:
            zeros += 1
        elif direction == -1 and num % 100 >= count:
            zeros += 1
        
        count += direction * num
        count = count % 100
    return zeros

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data.txt")
    print("First 5:", input_data[:5])
    print("Zerocount:", zerocount(input_data))
