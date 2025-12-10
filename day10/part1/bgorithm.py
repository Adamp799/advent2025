from pathlib import Path
from itertools import product
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(' ') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def find_button_combination(manual): 
    for machine in manual:
        light_diagram = machine[0]
        joltages = machine[-1] 
        button_wirings = [[int(x) for x in s.strip("()").split(",") if x.strip()] for s in machine[1:-1]]
        combos = list(product([0, 1], repeat=len(button_wirings)))
        #make a list of valid buttons 
        for combo in combos:
            [button for binary, button in zip(combo, button_wirings) if binary]
            
            

    print(light_diagram)
    print(joltages)
    print(button_wirings)
    return 0
            
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Total Button Presses:", find_button_combination(input_data))


#def button_checker(button_combo):
    # make button combo a list of e.g. [0, 0, 1, 1, 0, 1] scaled to the length of the list of buttons and if we encounter 
    #for i in button_combo