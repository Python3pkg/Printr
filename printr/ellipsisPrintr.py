class EllipsisPrinter():
    def __init__(self, string, max=5):
        self.string = string
        self.max = max
        self.count = -1

    def update(self, commit=False):
        self.clear()
        ellipsis = "." * self.count
        ending = '\r' if not commit else '\n'
        print(self.string + ellipsis, end=ending)
        if self.count >= self.max:
            self.zero()
        self.count += 1

    def zero(self):
        self.count = -1

    def commit(self):
        print()

    def clear(self):
        print(' ' * (len(self.string) + self.max), end='\r')