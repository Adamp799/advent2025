from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def max_joltage(line):
    digits_left = 12
    digit = -1
    while not digits_left:
        digit_list = [int(i) for i in line]
        digit = max(digit_list[digit + 1 : -1 * digits_left])
        counter += counter * 10 + digit
        digits_left -= 1
    return counter

def max_joltage_sum(digits):
    count = 0
    for line in digits:
        count += max_joltage(line, use)
    return count

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data.txt")
    print("First 5:", input_data[:3])
    print("Zerocount:", max_joltage_sum(input_data))