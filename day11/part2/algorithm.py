from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(' ') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def find_paths(input_data):
    node_dict = {n[0].strip(':') : n[1:] for n in input_data}
    return depth_first_search(node_dict, 'svr', 'out', set())

def depth_first_search(node_dict, current_node, target, visited):
    if current_node == target:
        if 'dac' in visited and 'fft' in visited: return 1
        else: return 0
    if current_node in visited: return 0
    visited.add(current_node)
    total_paths = 0
    for neighbor in node_dict.get(current_node, []):
        total_paths += depth_first_search(node_dict, neighbor, target, visited)
    visited.remove(current_node)
    return total_paths
   
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} nodes from data")
    print("Number of Paths:", find_paths(input_data))
