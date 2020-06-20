class Scanner:

    def __init__(self, source):
        self.source = source

        try:
            self.file = self.source
            self.eof = len(self.file) - 1
            self.index = 0

        except Exception as e:
            raise e

    def scan(self):

        if self.index < self.eof:
            char = self.file[self.index]
            self.index = self.index + 1

            return char

        return '\0'

    def rewind(self):
        if self.index == self.eof:
            return
        self.index -= 1

    def lookAhead(self):
        if self.index + 1 < self.eof:
            return self.file[self.index + 1]
        else:
            return '\0'
