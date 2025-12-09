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
                valid = True; ray_count = 0
                for j, coord in enumerate(coords): 
                    x_coord = int(coord[0]); y_coord = int(coord[1])
                    if (((y_coord <= min(int(y1), int(y2)) + 1 and int(edge_coords[j+1][1]) >= min(int(y1), int(y2)) + 1) or 
                        (y_coord >= min(int(y1), int(y2)) + 1 and int(edge_coords[j+1][1]) <= min(int(y1), int(y2)) + 1)) and 
                        (x_coord == int(edge_coords[j+1][0]) and x_coord > min(int(x1), int(x2)))):
                        ray_count += 1

                    if coord in ([x1, y1], [x2, y2], [x1, y2], [x2, y1]): continue
        
                    if (   (min(int(x1), int(x2)) < x_coord < max(int(x1), int(x2)) and
                            min(int(y1), int(y2)) < y_coord < max(int(y1), int(y2))) or 

                            (((x_coord == min(int(x1), int(x2)) and int(edge_coords[j+1][0]) > x_coord) or 
                            (x_coord == max(int(x1), int(x2)) and int(edge_coords[j+1][0]) < x_coord) or
                            (x_coord < min(int(x1), int(x2)) and int(edge_coords[j+1][0]) > max(int(x1), int(x2))) or 
                            (x_coord > max(int(x1), int(x2)) and int(edge_coords[j+1][0]) < min(int(x1), int(x2)))) and 
                            (y_coord > min(int(y1), int(y2)) and y_coord < max(int(y1), int(y2)))) or 

                            (((y_coord == min(int(y1), int(y2)) and int(edge_coords[j+1][1]) > y_coord) or
                            (y_coord == max(int(y1), int(y2)) and int(edge_coords[j+1][1]) < y_coord) or 
                            (y_coord < min(int(y1), int(y2)) and int(edge_coords[j+1][1]) > max(int(y1), int(y2))) or 
                            (y_coord > max(int(y1), int(y2)) and int(edge_coords[j+1][1]) < min(int(y1), int(y2)))) and 
                            (x_coord > min(int(x1), int(x2)) and x_coord < max(int(x1), int(x2))))   ):

                        valid = False
                        break
                print(ray_count)
                if valid and ray_count % 2 == 1: max_area = new_area; print(f"New max area {max_area} with corners ({x1},{y1}) and ({x2},{y2})")
    return max_area
            
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Largest Rectangle:", find_largest_rectangle(input_data))
