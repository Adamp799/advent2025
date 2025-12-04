from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"

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
    count_arr = [[0 * width] * height]
    
    curr_row = 0
    curr_col = 0
    unaccessible_count = 0
    rolls_count = 0
    for row in input_data:
        for char in row:
            if char == '@':
                rolls_count += 1
                count_arr[min(curr_row + 1, height)][curr_col] += 1
                count_arr[min(curr_row + 1, height)][min(curr_col + 1, width)] += 1
                count_arr[min(curr_row + 1, height)][max(curr_col - 1, 0)] += 1
                count_arr[curr_row][min(curr_col + 1, width)] += 1
                count_arr[curr_row][max(curr_col - 1, 0)] += 1
                count_arr[max(curr_row - 1, 0)][curr_col] += 1
                count_arr[max(curr_row - 1, 0)][min(curr_col + 1, width)] += 1
                count_arr[max(curr_row - 1, 0)][max(curr_col - 1, 0)] += 1
            curr_col += 1
            if count_arr[curr_row][curr_col] == 4: 
                unaccessible_count += 1
        curr_row += 1
    return rolls_count - unaccessible_count

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("First 5:", input_data[:5])
    print("Accessible Rolls:", count_rolls(input_data))
