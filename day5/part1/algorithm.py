from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            raw_lines = [line.rstrip("\n") for line in f]
            idx = raw_lines.index("") 
            return [raw_lines[:idx], raw_lines[idx+1:]]
        return None
    except FileNotFoundError:
        return []

def check_ingredients(ranges=None, ids = None):
    if ranges or ids is None: return 0
    invalid_sum = 0
    for id_range in input_data:
        min_id = int(id_range.split("-")[0])
        max_id = int(id_range.split("-")[1])
        for id_num in range(min_id, max_id + 1):
            s = str(id_num)
            if len(s) % 2: continue
            if s[:int(len(s)/2)] == s[int(len(s)/2):]:
                invalid_sum += id_num
    return invalid_sum

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {input_data} from data")
    print("Fresh Ingredients:", check_ingredients(input_data[0], input_data[1]))
