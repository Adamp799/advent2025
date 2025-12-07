from pathlib import Path
DATA_PATH = Path(__file__).parent / "data1.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def tachyon_beam(input_data):
    beam_locations = set()
    beam_locations.add(input_data[0].index('S'))
    timelines_triangle = {input_data[0].index('S') : 1}
    for line in input_data[1:]:
        splitters = {i for i, char in enumerate(line) if char == '^'}
        intersections = beam_locations.intersection(splitters)
        beam_locations.update({y for x in intersections for y in (x - 1, x + 1) if 0 <= y <= len(line) - 1})
        beam_locations.difference_update(intersections)
        for i in intersections: 
            temp = timelines_triangle 
            timelines_triangle.clear()
            timelines_triangle[i - 1] = temp.get(i - 1, 0) + temp[i]
            timelines_triangle[i + 1] = temp.get(i + 1, 0) + temp[i]
    return sum(timelines_triangle.values())

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Total Timelines:", tachyon_beam(input_data))
