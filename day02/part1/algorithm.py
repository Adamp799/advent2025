from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            id_ranges = [id_range.strip() for id_range in f.read().strip().split(",")]
            return id_ranges
    except FileNotFoundError:
        return []

def id_check(input_data=None):
    if input_data is None: return 0
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
    print("Invalid ID sum:", id_check(input_data))
