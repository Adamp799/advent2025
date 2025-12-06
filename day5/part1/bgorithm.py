from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            raw_lines = [line.rstrip("\n") for line in f]
            idx = raw_lines.index("") 
            return [raw_lines[:idx], raw_lines[idx+1:]]
        return None
    except FileNotFoundError:
        return []


def total_fresh(ranges, numbers):
    bounds_list = []
    for i in ranges:
        x = i.split('-')
        bounds_list.append([int(x[0]), int(x[1])])
    
    print(bounds_list)
    
    total = 0

    int_nums = [int(num) for num in numbers]
    print(int_nums)
    for i in int_nums:
        for tup in bounds_list:
            if i <= tup[1] and i >= tup[0]:
                total += 1
                break
            
    
    return total


if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {input_data} from data")
    print("Fresh Ingredients:", total_fresh(input_data[0], input_data[1]))