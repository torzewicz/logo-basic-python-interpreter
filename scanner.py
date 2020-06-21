class Scanner:

    def __init__(self, input):
        self.input = input
        self.index = 0

    def scan_and_shift(self):

        if self.index < len(self.input):
            current_char = self.input[self.index]
            self.index += 1
            return current_char
        else:
            return '\0'

    def unshift(self):
        if self.index == len(self.input):
            return
        else:
            self.index -= 1
