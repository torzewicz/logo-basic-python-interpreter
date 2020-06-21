from logo_keywords import Keyword


class Scanner:

    def __init__(self, raw_input):
        self.index = 0
        self.input = raw_input

    def get_logo_char(self):
        scanned_value = self.scan_and_shift()

        if scanned_value in " \t \n":
            scanned_value = self.scan_and_shift()

            while scanned_value in " \t \n":
                scanned_value = self.scan_and_shift()
            self.unshift()
            return None

        logo_char = {
            "value": scanned_value,
            "type": None
        }

        if scanned_value is '\0':
            logo_char["type"] = 'END'
            return logo_char

        if scanned_value.isalpha():
            scanned_value = self.scan_and_shift()

            while scanned_value.isalpha():
                logo_char["value"] += scanned_value
                scanned_value = self.scan_and_shift()

            self.unshift()

            if logo_char["value"] in [e.value for e in Keyword]:
                logo_char["type"] = 'KEYWORD'
            return logo_char

        if scanned_value.isnumeric():
            logo_char["type"] = 'NUMBER'
            scanned_value = self.scan_and_shift()

            while scanned_value.isnumeric():
                logo_char["value"] += scanned_value
                scanned_value = self.scan_and_shift()
            self.unshift()
            return logo_char

        if scanned_value in ["[", "]"]:
            logo_char["type"] = scanned_value
            return logo_char

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