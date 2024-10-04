class Nirmal:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
            
        self.step = step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        else:
            value = self.current
            self.current += self.step
            return value