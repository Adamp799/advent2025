from pathlib import Path
from itertools import product
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(' ') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def find_button_combination(manual): 
    min_presses_list = []
    for machine in manual:
        joltages = machine[-1] 
        light_diagram = [0 if c == "." else 1 for c in machine[0].strip("[]")]
        button_wirings = [[int(x) for x in s.strip("()").split(",") if x.strip()] for s in machine[1:-1]]
        permutations = list(product([0, 1], repeat=len(button_wirings)))
        min_presses = float('inf')
        for perm in permutations: 
            lights = [0] * len(light_diagram)
            for button_index, button_state in enumerate(perm):
                wiring = button_wirings[button_index]
                for light_index in wiring:
                    lights[light_index] ^= button_state
            if lights == light_diagram:
                presses = sum(perm)
                if presses < min_presses: min_presses = presses
        if min_presses != float('inf'): min_presses_list.append(min_presses)
    return sum(min_presses_list)
            
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Total Button Presses:", find_button_combination(input_data))
