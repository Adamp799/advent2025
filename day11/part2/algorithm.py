from pathlib import Path
from functools import lru_cache
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(' ') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def calculate_paths(input_data):
    graph = {n[0].strip(':') : n[1:] for n in input_data}
    svr_to_dac = count_paths(graph, "svr", "dac", forbid={"fft"})
    svr_to_fft = count_paths(graph, "svr", "fft", forbid={"dac"})
    dac_to_fft = count_paths(graph, "dac", "fft")
    fft_to_dac = count_paths(graph, "fft", "dac")
    dac_to_out = count_paths(graph, "dac", "out")
    fft_to_out = count_paths(graph, "fft", "out")
    return (svr_to_dac * dac_to_fft * fft_to_out + svr_to_fft * fft_to_dac * dac_to_out)

def count_paths(graph, start, end, forbid=None):
    if forbid is None: forbid = set()
    forbid = frozenset(forbid)
    @lru_cache(None)
    def dfs(node):
        if node == end: return 1
        total = 0
        for neighbor in graph.get(node, []):
            if neighbor not in forbid: total += dfs(neighbor)
        return total

    if start in forbid: return 0
    return dfs(start)
   
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} nodes from data")
    print("Number of Paths:", calculate_paths(input_data))
