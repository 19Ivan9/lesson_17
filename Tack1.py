def with_index(iterable,start=0):
    obj = iter(iterable)
    i = 0
    while i < len(iterable):
        yield start, next(obj)
        start += 1
        i += 1