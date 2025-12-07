def tachyon_beam(input_data):
    total_splits = 0
    beam_locations = set()
    beam_locations.add(input_data[0].index('S'))
    for line in input_data[1:]:
        splitters = {i for i, char in enumerate(line) if char == '^'}
        intersections = beam_locations.intersection(splitters)
        total_splits += len(intersections)
        beam_locations.update({y for x in intersections for y in (x - 1, x + 1) if 0 <= y <= len(line) - 1})
    return total_splits