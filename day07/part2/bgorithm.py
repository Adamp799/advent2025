from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def tachyon_beam(input_data):
    total_splits = 0
    beam_locations = {}
    beam_locations[input_data[0].index('S')] = 1
    # we need a dict for the beam locations with index: count

    for line in input_data[1:]:
        splitters = {i for i, char in enumerate(line) if char == '^'}

        #c = set(beam_locations.keys()) # set of keys from beams
        #d = set(splitters.keys()) # set of keys from splitters

        #e = c.intersection(d) #  intersection of the two sets
        #res = {k: beam_locations[k] for k in e}
        intersections = beam_locations.keys().intersection(splitters)
        total_splits += len(intersections)
        beam_locations.update({x - 1 for x in intersections : beam_locations[x]})
        # for y in (x - 1, x + 1) if 0 <= y <= len(line) - 1 : beam_locations[x - 1]}
        beam_locations.difference_update(intersections)
    return total_splits

if __name__ == "__main__":
    input_data = read_input()
    print(f"Read {len(input_data)} lines from data")
    print("Total Splits:", tachyon_beam(input_data))
