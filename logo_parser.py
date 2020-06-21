import pygame
import sys

from logo_keywords import Keyword
from typecreator import TypeCreator
from turtle import Turtle


class LogoParser:

    def __init__(self):
        self.token_list = []
        self.index = -1
        self.turtle = None
        self.logo_init()

    def apply_user_input(self, source):
        self.token_list = []
        self.fill_token_list(source)
        self.index = -1
        self.parse()

    def fill_token_list(self, source):
        type_creator = TypeCreator(source)
        while True:
            token = type_creator.get_token()
            if token is not None:
                self.token_list.append(token)
                if token.type == 'Eof':
                    break

    def check_next_token(self):
        if self.index + 1 < len(self.token_list):
            return self.token_list[self.index + 1]
        else:
            return None

    def get_current_token(self):
        return self.token_list[self.index]

    def get_next_token(self):
        self.index += 1
        return self.token_list[self.index]

    def logo_init(self):
        pygame.init()
        self.turtle = Turtle()
        self.turtle.draw()
        pygame.display.flip()
        pygame.display.set_caption("Logo")

    def parse(self):

        self.parse_characters()
        token_ahead = self.check_next_token()
        while token_ahead is not None and token_ahead.type == 'Keyword':
            self.parse_characters()
            token_ahead = self.check_next_token()

    def parse_characters(self):

        next_token = self.check_next_token()
        if next_token is None or next_token.value not in [e.value for e in Keyword]:
            print("Incorrect input")
            return

        if next_token.value in ['fd', 'bk', 'rt', 'lt']:
            self.shift_and_match()
            if self.shift_matching_numeric() is False:
                return

            if next_token.value == 'fd':
                self.turtle.mv_forward(int(self.get_current_token().value))
            if next_token.value == 'bk':
                self.turtle.move_backward(int(self.get_current_token().value))
            if next_token.value == 'lt':
                self.turtle.rotate(int(self.get_current_token().value))
            if next_token.value == 'rt':
                self.turtle.rotate(int(-1 * int(self.get_current_token().value)))

        if next_token.value in ['pu', 'pd', 'ht', 'st']:
            self.shift_and_match()

            if next_token.value == 'pu':
                self.turtle.pen_up()
            if next_token.value == 'pd':
                self.turtle.pen_down()
            if next_token.value == 'st':
                self.turtle.show_turtle()
            if next_token.value == 'ht':
                self.turtle.hide_turtle()

        if next_token.value in ['repeat']:
            self.shift_and_match()
            if self.shift_matching_numeric() is False:
                return

            times = int(self.get_current_token().value)

            if self.shift_and_match('[') is False:
                return
            go_back_and_repeat_index = self.index
            for i in range(0, times):
                self.parse()
                if i != times - 1:
                    self.index = go_back_and_repeat_index
            if self.shift_and_match(']') is False:
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.turtle.draw()
        pygame.display.flip()

    def shift_matching_numeric(self):

        token = self.get_next_token()
        if not token.value.isnumeric():
            print("Expected numeric but got " + token.type)
            return False
        else:
            return True

    def shift_and_match(self, expected_token_type=None):

        token = self.get_next_token()
        if expected_token_type is None:
            return True
        if token.type != expected_token_type:
            print("Expected token type " + expected_token_type + " but got " + token.type)
            return False
