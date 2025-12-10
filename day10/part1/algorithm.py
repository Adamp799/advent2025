from pathlib import Path
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
    return 0
            
if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Total Button Presses:", find_button_combination(input_data))
