from pathlib import Path
from scipy.spatial import KDTree
import math
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(',') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def shortest_k_pairs(points, k=1000):
    tree = KDTree(points)
    dists, idxs = tree.query(points, k=len(points)+1)
    pairs = []
    for i in range(len(points)):
        for n in range(1, len(points)+1):  
            j = idxs[i][n]
            if i < j: pairs.append(((i, j), dists[i][n]))
    pairs.sort(key=lambda x: x[1])
    return pairs[:k]

def junction_boxes(points): 
    pairs = shortest_k_pairs(points)
    circuits = []
    for (i, j), dist in pairs: 
        matching_circuits = [circuit for circuit in circuits if i in circuit or j in circuit]
        if not matching_circuits: circuits.append(set([i, j]))
        else:
            merged = set([i, j])
            for circuit in matching_circuits:
                merged.update(circuit)
                circuits.remove(circuit)
            circuits.append(merged)
    return math.prod(sorted([len(circuit) for circuit in circuits], reverse=True)[:3])
            
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Junction Product:", junction_boxes(input_data))
