from printr.utils import write

class EllipsisPrintr():
    def __init__(self, string, max=3, erase_after=False):
        self.string = string
        self.max = max
        self.count = -1
        self.erase_after = erase_after

    def update(self, commit=False):
        self.clear()
        ellipsis = "." * self.count
        write(self.string + ellipsis, commit=commit)
        if self.count >= self.max:
            self.zero()
        self.count += 1

    def zero(self):
        self.count = -1

    def commit(self):
        print()

    def clear(self):
        print(' ' * (len(self.string) + self.max), end='\r')

    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        if self.erase_after:
            self.clear()
        self.commit()