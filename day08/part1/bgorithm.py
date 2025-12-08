import numpy as np
from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(',') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def distance(a, b):
    return np.sqrt((int(a[0]) - int(b[0]))**2 + (int(a[1]) - int(b[1]))**2 + (int(a[2]) - int(b[2]))**2)

def distance_matrix(input):
    length = len(input)
    distances = np.full((length, length), float('inf'))
    for i, point in enumerate(input):
        for j, other in enumerate(input):
            if point[0] < other[0]:
                distances[i, j] = distance(point, other)
    
    return distances

def circuits(input):
    n = 1000
    matrix = distance_matrix(input)
    smallest_n = np.sort(matrix.ravel())[:n]
    chains = [[1001, 1002]]
    # find min within array then update to float('inf')
    for k in range(n):
        mini = float('inf')
        for i, row in enumerate(matrix):
            for j, distance in enumerate(row):
                if mini > distance:
                    mini = distance
                    x = i
                    y = j
        print(mini)
        
        matrix[x, y] = float('inf')
        #search if min is within existing chain
        k = len(chains)
        count = 0
        temp_chains = chains
        for idx, chain in enumerate(chains):
            if x in chain:
                temp_chains[idx].append(y)
                break
            elif y in chain:
                temp_chains[idx].append(x)
                break
            count += 1
        chains = temp_chains

        if count == k:
            chains.append([x, y])
    #return product of three larges chains
    chain_lengths = [len(chain) for chain in chains]
    first = max(chain_lengths)
    chain_lengths = [i for i in chain_lengths if i != first]
    second = max(chain_lengths)
    chain_lengths = [i for i in chain_lengths if i != second]
    third = max(chain_lengths)

    return first * second * third
            

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Total Splits:", circuits(input_data))