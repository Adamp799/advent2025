from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def max_joltage(line, digits_left):
    if digits_left == 1:
        return max([int(i) for i in line])
    digit_list = [int(i) for i in line]
    digit = max(digit_list[: -1 * (digits_left - 1)])
    idx = digit_list.index(digit)
    line = line[idx + 1:]
    return digit * (10**(digits_left - 1)) + max_joltage(line, digits_left - 1)

def max_joltage_sum(digits):
    count = 0
    for line in digits:
        count += max_joltage(line, 12)
    return count

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data.txt")
    print("First 5:", input_data[:5])
    print("Max Joltage:", max_joltage_sum(input_data))
