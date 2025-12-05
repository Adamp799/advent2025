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

    rolls_total = 0
    for i in range(height):
        for j in range(width):
            if count_arr[i][j] < 4: 
                rolls_total += 1
                input_data[i] = input_data[i][:j] + 'x' + input_data[i][j+1:]
    if rolls_total == 0: return 0
    else: return rolls_total + count_rolls(input_data)

def safe_list_increment(count_arr, i1, i2):
    if i1 is None or i2 is None: return
    if 0 <= i1 < len(count_arr) and 0 <= i2 < len(count_arr[i1]):
        count_arr[i1][i2] += 1

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Removable Rolls:", count_rolls(input_data))
