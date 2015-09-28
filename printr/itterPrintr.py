from exceptions import FormattingError


class ItterPrintr():
    def __init__(self, string, maxValue, start, diff=1):
        self.string = string
        self.maxValue = maxValue
        self.start = start
        self.diff = diff
        self.value = self.start
        self.buildString()

    def buildString(self):
        try:
            return self.string.format(c=self.value, m=self.maxValue)
        except:
            raise FormattingError()

    def reachedLimit(self):
        return self.maxValue <= self.value

    def update(self, inc=True):
        ending = '\r' if not self.reachedLimit() else '\n'
        print(self.buildString(), end=ending)
        if inc:
            self.inc()

    def inc(self):
        self.value += self.diff