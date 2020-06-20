from keyword import Keyword
from scanner import Scanner
from token import Token

eof_key = '\0'


class Tokenizer:

    def __init__(self, source):
        self.scanner = Scanner(source)

    def getToken(self):
        char = self.getChar()
        # print char

        if char in " \t \n":
            # print "WHITESPACE"
            char = self.getChar()

            while char in " \t \n":
                char = self.getChar()
            self.scanner.rewind()
            return None

        token = Token(char)
        # print "TOKEN CREATED"

        if char in eof_key:
            # print "EOF TOKEN"
            token.type = 'Eof'
            return token

        if char.isalpha():
            # print "IDENTIFIER TOKEN"
            token.type = 'Indentifier'
            char = self.getChar()

            while char.isalnum():
                token.value += char
                char = self.getChar()

            self.scanner.rewind()

            if token.value in [e.value for e in Keyword]:
                token.type = 'Keyword'
            return token

        if char.isnumeric():
            # print "NUMERIC TOKEN"
            token.type = 'Numeric'
            char = self.getChar()

            while char.isnumeric():
                token.value += char
                char = self.getChar()
            self.scanner.rewind()
            return token

        if char in ["[", "]"]:
            # print "OPERATOR TOKEN"
            token.type = char
            return token

    def getChar(self):
        char = self.scanner.scan()
        self.charAhead = char + self.scanner.lookAhead()
        return char
