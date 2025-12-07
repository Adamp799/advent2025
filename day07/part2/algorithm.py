from pathlib import Path
DATA_PATH = Path(__file__).parent / "example.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def tachyon_beam(input_data):
    beam_locations = set()
    beam_locations.add(input_data[0].index('S'))
    timelines_triangle = {next(iter(beam_locations)) : 1}
    temp_triangle = {}
    for line in input_data[1:]:
        splitters = {i for i, char in enumerate(line) if char == '^'}
        intersections = beam_locations.intersection(splitters)
        beam_locations.update({y for x in intersections for y in (x - 1, x + 1) if 0 <= y <= len(line) - 1})
        beam_locations.difference_update(intersections)
        #print(intersections)
        print(timelines_triangle)
        if len(intersections) > 0: 
            temp_triangle = {} | timelines_triangle
            timelines_triangle.clear()
        for i in intersections: 
            #print(temp_triangle)
            timelines_triangle[i - 1] = temp_triangle.get(i - 2, 0) + temp_triangle[i]
            timelines_triangle[i + 1] = temp_triangle.get(i + 2, 0) + temp_triangle[i]
    return sum(timelines_triangle.values())

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Total Timelines:", tachyon_beam(input_data))
