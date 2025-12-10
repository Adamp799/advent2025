from pathlib import Path
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(' ') for line in f if line.strip()]
    except FileNotFoundError:
        return []

def find_button_combination(manual): 
    min_presses_list = []
    for machine in manual:
        joltages = [int(x) for x in machine[-1].strip("{}").split(",") if x.strip()]
        button_wirings = [[int(x) for x in s.strip("()").split(",") if x.strip()] for s in machine[1:-1]]
        A = [[0]*len(button_wirings) for _ in range(len(joltages))]
        for i in range(len(button_wirings)):
            for j in range(len(joltages)):
                A[j][i] = 1 if j in button_wirings[i] else 0
        c = np.ones(len(button_wirings)) 
        A_eq = np.array(A)
        b_eq = np.array(joltages)
        constraints = LinearConstraint(A_eq, b_eq, b_eq)
        integrality = np.ones(len(button_wirings))  
        bounds = Bounds(lb=0)  
        res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
        print("Optimal value:", res.fun)
        print("Variables [a,b,c,d,e,f]:", res.x)
        min_presses_list.append(int(res.fun))
    return sum(min_presses_list)
            
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Total Button Presses:", find_button_combination(input_data))
