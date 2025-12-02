from pathlib import Path
DATA_PATH = Path(__file__).parent / "data2.txt"

def read_input(path=DATA_PATH):
    try:
        with open(path, "r") as f:
            return f
    except FileNotFoundError:
        return []

def invalid_sum(input_data=None):
    # split based on commaa
    range_list = input_data.split(',')
    count = 0
    # loop through new list and split at the hyphens then put into range function
    for interval in range_list:
        x = interval.split('-')
        maxi = int(x[0])
        mini = int(x[1])
        for i in range(maxi, mini + 1):
            if len(i) % 2:
                continue
            str_i = str(i)
            if str_i[:len(str_i)/2] == str_i[len(str_i)/2:]:
                count += i
    return count

    # check all numbers in range by first checking if they have even number of digits
    # then check if you split halfway, the two numbers are equal
    # update invalid count
    # return invalid count

if __name__ == "__main__":
    input_data = read_input()
    print("First 5:", input_data[:5])
    print("Invalid Sum:", invalid_sum(input_data))