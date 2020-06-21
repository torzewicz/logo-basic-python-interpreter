class Scanner:

    def __init__(self, source):
        try:
            self.source = source
            self.index = 0

        except Exception as e:
            raise e

    def scan_and_shift(self):

        if self.index < len(self.source):
            char = self.source[self.index]
            self.index = self.index + 1
            return char
        else:
            return '\0'

    def unshift(self):
        if self.index == len(self.source):
            return
        else:
            self.index -= 1
