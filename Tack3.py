class Iterator:
    def __init__(self,value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.value):
            raise StopIteration('End')
        return self.value[self.index - 1]

    def __getitem__(self, item):
        return self.value[item]