from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip("\n") for line in f if line.strip()]
    except FileNotFoundError:
        return []

def perform_calculations(input_data):
    total = 0 
    curr_operation = " "
    for i in range(len(input_data[-1])): 
        if input_data[-1][i] == "+":
            curr_operation = "+"
        elif input_data[-1][i] == "*":
            curr_operation = "*"

        num_string = ""
        for j in range(len(input_data) - 1):
            num_string += input_data[j][i]

        #if curr_operation == "+":
            #for j in range(len(input_data) - 1):
              #  total += int(input_data[j][i])
        #elif curr_operation == "*": 
           # subtotal = 1
            ##for j in range(len(input_data) - 1):
                #subtotal *= int(input_data[j][i])
           # total += subtotal
    return total

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print(len(input_data[-1]), len(input_data[0]))
    print(input_data)
    print("Grand Total:", perform_calculations(input_data))
