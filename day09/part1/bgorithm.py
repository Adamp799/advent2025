from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip().split(',') for line in f if line.strip()]
    except FileNotFoundError:
        return []


def area(coord1, coord2):
    return (abs(int(coord1[0]) - int(coord2[0])) + 1) * (abs(int(coord1[1]) - int(coord2[1])) + 1)

def maximum_area(data):
    maxi = 0
    for point1 in data:
        for point2 in data:
            maxi = max(area(point1, point2), maxi)

    return maxi



if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} coordinates from data")
    print("Largest Rectangle:", maximum_area(input_data))
