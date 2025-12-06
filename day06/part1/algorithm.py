from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            lines = [line.strip().split() for line in f if line.strip()]
            return lines
    except FileNotFoundError:
        return []

def perform_calculations(input_data):
    total = 0 
    for i in range(len(input_data[0])): 
        if input_data[-1][i] == "+":
            for j in range(len(input_data) - 1):
                total += int(input_data[j][i])
        else: 
            subtotal = 1
            for j in range(len(input_data) - 1):
                subtotal *= int(input_data[j][i])
            total += subtotal
    return total

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data[0])} calculations from data")
    print("Grand Total:", perform_calculations(input_data))
