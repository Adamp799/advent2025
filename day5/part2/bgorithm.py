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

def merge(intervals):
    if not intervals:
        return []

    # Sort the intervals based on the starting points
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged_intervals[-1]

        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Otherwise, add the current interval to the merged list
            merged_intervals.append(current)

    return merged_intervals

def total_fresh(ranges):
    intervals = []
    
    for i in ranges:
        x = i.split('-')
        intervals.append([int(x[0]), int(x[1])])
    
    total = 0
    for i in merge(intervals):
        total += i[1] - i[0] + 1
    
    return total

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {input_data} from data")
    print("Fresh Ingredients:", total_fresh(input_data[0]))