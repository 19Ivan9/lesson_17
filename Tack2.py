def in_range(start,end,step=0):
    if step == 0:
        sequence = []
        while start < end:
            sequence.append(start)
            start += 1
        return sequence
    sequence = [start]
    while start < end:
        start += step
        sequence.append(start)
    return sequence