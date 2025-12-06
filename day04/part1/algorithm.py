from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def count_rolls(input_data=None):
    if input_data is None: return 0
    height = len(input_data)
    width = len(input_data[0])
    count_arr = [[0] * width for _ in range(height)]
    curr_row = 0; curr_col = 0
    for row in input_data:
        for char in row:
            if char == '@':
                safe_list_increment(count_arr, curr_row + 1, curr_col)
                safe_list_increment(count_arr, curr_row + 1, curr_col + 1)
                safe_list_increment(count_arr, curr_row + 1, curr_col - 1)
                safe_list_increment(count_arr, curr_row, curr_col + 1)
                safe_list_increment(count_arr, curr_row, curr_col - 1)
                safe_list_increment(count_arr, curr_row - 1, curr_col)
                safe_list_increment(count_arr, curr_row - 1, curr_col + 1)
                safe_list_increment(count_arr, curr_row - 1, curr_col - 1)
            else: count_arr[curr_row][curr_col] += 100
            curr_col += 1
        curr_col = 0
        curr_row += 1
    return sum(1 for row in count_arr for count in row if count < 4)

def safe_list_increment(count_arr, i1, i2):
    if i1 is None or i2 is None: return
    if 0 <= i1 < len(count_arr) and 0 <= i2 < len(count_arr[i1]):
        count_arr[i1][i2] += 1

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Accessible Rolls:", count_rolls(input_data))
