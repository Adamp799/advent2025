from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip("\n") for line in f if line.strip()]
    except FileNotFoundError:
        return []

def construct_nums(input_data):
    total = 0 
    curr_operation = " "
    num_strings = []
    for i in range(len(input_data[-1])): 
        if input_data[-1][i] == "+":
            curr_operation = "+"
        elif input_data[-1][i] == "*":
            curr_operation = "*"

        num_string = ""
        for j in range(len(input_data) - 1):
            num_string += input_data[j][i]
        if num_string.strip() != "":
            num_strings.append(num_string.strip() + curr_operation)
    return num_strings

def perform_calculations(num_strings):
    grand_total = 0
    subtotal = 1
    multiplier = False
    for num_str in num_strings:
        if num_str[-1] == "+":
            if multiplier: grand_total += subtotal
            subtotal = 1
            multiplier = False
            grand_total += int(num_str[:-1])
        else: 
            multiplier = True
            subtotal *= int(num_str[:-1])
    return grand_total

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    constructed_nums = construct_nums(input_data)
    print("Constructed Numbers:", constructed_nums)
    print("Constructed Numbers Length:", len(constructed_nums))
    print("Grand Total:", perform_calculations(constructed_nums))
