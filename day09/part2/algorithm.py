from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(',') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def find_largest_rectangle(coords): 
    max_area = float('-inf')
    edge_coords = [coord for coord in coords + [coords[0]]] 
    for i, [x1, y1] in enumerate(coords):
        for x2, y2 in coords[i+1:]:
            new_area = (abs(int(x2) - int(x1)) + 1) * (abs(int(y2) - int(y1)) + 1)
            if new_area > max_area: 
                valid = True
                for j, coord in enumerate(coords): 
                    if coord in ([x1, y1], [x2, y2], [x1, y2], [x2, y1]): continue
                    x_coord = int(coord[0]); y_coord = int(coord[1])
                    if ((min(int(x1), int(x2)) < x_coord < max(int(x1), int(x2)) and
                            min(int(y1), int(y2)) < y_coord < max(int(y1), int(y2))) or 
                            (x_coord == min(int(x1), int(x2)) and int(edge_coords[j+1][0]) > x_coord) or 
                            (x_coord == max(int(x1), int(x2)) and int(edge_coords[j+1][0]) < x_coord) or
                            (y_coord == min(int(y1), int(y2)) and int(edge_coords[j+1][1]) > y_coord) or
                            (y_coord == max(int(y1), int(y2)) and int(edge_coords[j+1][1]) < y_coord) or 
                            ((x_coord < min(int(x1), int(x2)) and int(edge_coords[j+1][0]) > max(int(x1), int(x2))) and 
                            (y_coord >= min(int(y1), int(y2)) and y_coord <= max(int(y1), int(y2)))) or 
                            ((y_coord < min(int(y1), int(y2)) and int(edge_coords[j+1][1]) > max(int(y1), int(y2))) and
                            (x_coord >= min(int(x1), int(x2)) and x_coord <= max(int(x1), int(x2))))):
                        valid = False
                        break
                if valid: max_area = new_area
    return max_area
            
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Largest Rectangle:", find_largest_rectangle(input_data))
