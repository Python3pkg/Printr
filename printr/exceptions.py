class FormattingError(Exception):
    message = "Provided string doesn't contain formatting placeholders for {c} and/or {m}"
    def __init__(self):
        super().__init__(self.message)

