from logo_keywords import Keyword
from scanner import Scanner


class TypeCreator:

    def __init__(self, source):
        self.scanner = Scanner(source)

    def get_logo_char(self):
        scanned_value = self.scanner.scan_and_shift()

        if scanned_value in " \t \n":
            scanned_value = self.scanner.scan_and_shift()

            while scanned_value in " \t \n":
                scanned_value = self.scanner.scan_and_shift()
            self.scanner.unshift()
            return None

        logo_char = {
            "value": scanned_value,
            "type": None
        }

        if scanned_value is '\0':
            logo_char["type"] = 'END'
            return logo_char

        if scanned_value.isalpha():
            scanned_value = self.scanner.scan_and_shift()

            while scanned_value.isalpha():
                logo_char["value"] += scanned_value
                scanned_value = self.scanner.scan_and_shift()

            self.scanner.unshift()

            if logo_char["value"] in [e.value for e in Keyword]:
                logo_char["type"] = 'KEYWORD'
            return logo_char

        if scanned_value.isnumeric():
            logo_char["type"] = 'NUMBER'
            scanned_value = self.scanner.scan_and_shift()

            while scanned_value.isnumeric():
                logo_char["value"] += scanned_value
                scanned_value = self.scanner.scan_and_shift()
            self.scanner.unshift()
            return logo_char

        if scanned_value in ["[", "]"]:
            logo_char["type"] = scanned_value
            return logo_char
