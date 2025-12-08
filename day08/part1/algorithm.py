from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"
from scipy.spatial import KDTree

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(',') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def junction_boxes(input_data):
    tree = KDTree(input_data)
    min_dist = float('inf')
    for i, p in enumerate(input_data):
        dist, idx = tree.query(p, k=2)

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Input Data:", input_data)
    print("Junction Product:", junction_boxes(input_data))
