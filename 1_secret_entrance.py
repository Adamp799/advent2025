def zerocount(x):
    count = 50
    zeros = 0
    for row in x:
        if row[0] == 'R':
            direction = 1
        else:
            direction = -1
        num = int(row[1:])
        count += direction * num
        if not count % 100:
            zeros += 1
    return zeros
