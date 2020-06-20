from turtle import Turtle

from keyword import Keyword
from tokenizer import Tokenizer
import sys, pygame

background_color = (169, 169, 169)


class LogoParser:

    def __init__(self, source):
        self.T = Tokenizer(source)
        self.tokenList = []
        self.createTokenList()
        self.dispTokenList()
        self.index = -1
        self.history = []

    def reInit(self, source):
        self.T = Tokenizer(source)
        self.tokenList = []
        self.createTokenList()
        self.dispTokenList()
        self.index = -1
        self.history = []

    def createTokenList(self):

        # print "TOKENIZER STEP"
        while True:
            token = self.T.getToken()
            if token is not None:
                token.display()
                self.tokenList.append(token)
                if token.type == 'Eof':
                    break

        # raw_input()

    def dispTokenList(self):
        for token in self.tokenList:
            token.display()

    def lookNextToken(self):
        try:
            return self.tokenList[self.index + 1]
        except IndexError as e:
            return None

    def currToken(self):
        return self.tokenList[self.index]

    def getNextToken(self):
        self.index += 1
        return self.tokenList[self.index]

    def graphInit(self):
        pygame.init()

        window_x = 600
        window_y = 600
        self.screen = pygame.display.set_mode((window_x, window_y))

        self.Turtle = Turtle(window_x, window_y)
        # self.Turtle.setImage(pygame.image.load("turtle.png"))

        self.screen.fill(background_color)
        self.Turtle.draw(self.screen)
        pygame.display.flip()
        pygame.display.set_icon(pygame.image.load("turtle.png"))
        pygame.display.set_caption(" Turtle")

    def parse(self):

        self.parseSentence()
        while True:
            tokenAhead = self.lookNextToken()
            if tokenAhead == None:
                break
            elif tokenAhead.type == 'Eof':
                break
            elif tokenAhead.type == 'Keyword':
                self.parseSentence()
            else:
                break

    def parseSentence(self):

        # parsing
        nextToken = self.lookNextToken()
        if nextToken.value not in [e.value for e in Keyword]:
            print("Invalid input")
            return
        if nextToken.value in ['fd', 'bk', 'rt', 'lt']:
            self.Match()
            if (self.matches_numeric() == -1):
                return

            # graphics
            if nextToken.value == 'fd':
                self.Turtle.mvForward(int(self.currToken().value), self.screen)
            if nextToken.value == 'bk':
                self.Turtle.mvBackward(int(self.currToken().value), self.screen)
            if nextToken.value == 'lt':
                self.Turtle.rotate(int(self.currToken().value))
            if nextToken.value == 'rt':
                self.Turtle.rotate(int(-1 * int(self.currToken().value)))

            self.history.append((nextToken.value, self.currToken().value))

        if nextToken.value in ['pu', 'pd', 'ht', 'st', 'penerase']:
            self.Match()
            if nextToken.value == 'pu':
                self.Turtle.penUp()
            if nextToken.value == 'pd':
                self.Turtle.penDown()
            if nextToken.value == 'st':
                self.Turtle.showTurtle()
            if nextToken.value == 'ht':
                self.Turtle.hideTurtle()
            self.history.append(nextToken.value)

        if nextToken.value in ['setcolor']:
            self.Match()
            try:
                # self.Match(NUMERIC)
                self.matches_numeric()
                red = int(self.currToken().value)
                # self.Match(NUMERIC)
                self.matches_numeric()
                green = int(self.currToken().value)
                # self.Match(NUMERIC)
                self.matches_numeric()
                blue = int(self.currToken().value)
                self.Turtle.setPenColor(red, green, blue)
                self.history.append((nextToken.value, red, green, blue))
            except ValueError as e:
                print(e)
        if nextToken.value in ['repeat']:
            self.Match()
            # self.Match(NUMERIC)
            self.matches_numeric()

            timesToLoop = int(self.currToken().value)

            self.Match('[')
            savedIndex = self.index
            for i in range(0, timesToLoop):
                self.parse()
                if i != timesToLoop - 1:
                    self.index = savedIndex
            self.Match(']')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        self.screen.fill(background_color)
        self.Turtle.draw(self.screen)
        pygame.display.flip()

    def matches_numeric(self):
        token = self.getNextToken()
        if not token.value.isnumeric():
            print("Expected numeric but got " + token.type)
            return -1

    def Match(self, expectedTokenType=None):
        token = self.getNextToken()
        if (expectedTokenType == None):
            return
        if (token.type != expectedTokenType):
            print("Expected token type " + expectedTokenType + " but got " + token.type)
            return -1
