from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(',') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def find_largest_rectangle(coords): 
    max_area = float('-inf')
    edge_coords = [coord for coord in coords + coords[0]] 
    valid = True
    for i, [x1, y1] in enumerate(coords):
        for x2, y2 in coords[i+1:]:
            new_area = (abs(int(x2) - int(x1)) + 1) * (abs(int(y2) - int(y1)) + 1)
            if new_area > max_area: 
                for i in range(0, len(edge_coords), 2):
                    X1, Y1 = edge_coords[i]
                    X2, Y2 = edge_coords[i+1]
                    if X1 == X2: 
                        if (min(int(x1), int(x2)) <= int(X1) <= max(int(x1), int(x2)) and
                            min(int(y1), int(y2)) <= int(Y1) <= max(int(y1), int(y2))):
                            valid = False
                            break
                    elif Y1 == Y2:
                        if (min(int(x1), int(x2)) <= int(X1) <= max(int(x1), int(x2)) and
                            min(int(y1), int(y2)) <= int(Y1) <= max(int(y1), int(y2))):
                            valid = False
                            break
                if valid: max_area = new_area
    return max_area
            
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Largest Rectangle:", find_largest_rectangle(input_data))
