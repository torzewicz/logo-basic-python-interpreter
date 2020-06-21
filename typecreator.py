from logo_char import LogoChar
from logo_keywords import Keyword
from scanner import Scanner


class TypeCreator:

    def __init__(self, source):
        self.scanner = Scanner(source)

    def get_token(self):
        char = self.scanner.scan_and_shift()

        if char in " \t \n":
            char = self.scanner.scan_and_shift()

            while char in " \t \n":
                char = self.scanner.scan_and_shift()
            self.scanner.unshift()
            return None

        logo_char = LogoChar(char)

        if char is '\0':
            logo_char.type = 'Eof'
            return logo_char

        if char.isalpha():
            char = self.scanner.scan_and_shift()

            while char.isalpha():
                logo_char.value += char
                char = self.scanner.scan_and_shift()

            self.scanner.unshift()

            if logo_char.value in [e.value for e in Keyword]:
                logo_char.type = 'Keyword'
            return logo_char

        if char.isnumeric():
            logo_char.type = 'Numeric'
            char = self.scanner.scan_and_shift()

            while char.isnumeric():
                logo_char.value += char
                char = self.scanner.scan_and_shift()
            self.scanner.unshift()
            return logo_char

        if char in ["[", "]"]:
            logo_char.type = char
            return logo_char
