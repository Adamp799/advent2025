from pathlib import Path

# Path to the input file next to this script
DATA_PATH = Path(__file__).parent / "data.txt"


def read_input(path=DATA_PATH):
    """Read the input file and return a list of non-empty, stripped lines.

    Returns an empty list if the file is not found.
    """
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


# Variable requested: contains the input file lines
input_data = read_input()


def zerocount(x=None):
    """Count how many times 'count' is a multiple of 100 while processing moves.

    If x is None, use the module-level `input_data` loaded from `data.txt`.
    """
    if x is None:
        x = input_data

    count = 50
    zeros = 0
    for row in x:
        if not row:
            continue
        direction = 1 if row[0] == 'R' else -1
        num = int(row[1:])
        count += direction * num
        if count % 100 == 0:
            zeros += 1
    print("ZEROS:", zeros)
    return zeros


if __name__ == "__main__":
    print(f"Read {len(input_data)} lines from data.txt")
    print("First 5:", input_data[:5])
    zerocount()
