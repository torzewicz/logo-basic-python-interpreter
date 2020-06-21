import pygame
import sys

from logo_keywords import Keyword
from type_creator import TypeCreator
from turtle import Turtle


class LogoParser:

    def __init__(self):
        self.token_list = None
        self.index = 0
        self.turtle = None
        self.logo_init()

    def apply_user_input(self, user_input):
        self.token_list = []
        self.fill_list(user_input)
        self.index = -1
        self.init_parser()

    def fill_list(self, user_input):
        type_creator = TypeCreator(user_input)
        logo_char = type_creator.get_logo_char()
        received_end = False
        while not received_end:
            if logo_char is not None:
                self.token_list.append(logo_char)
                if logo_char["type"] == 'END':
                    received_end = True
            if not received_end:
                logo_char = type_creator.get_logo_char()

    def check_next_token(self):
        if self.index + 1 < len(self.token_list):
            return self.token_list[self.index + 1]
        else:
            return None

    def get_current_token(self):
        return self.token_list[self.index]

    def init_parser(self):

        self.parse_characters()
        next_token = self.check_next_token()
        while next_token is not None and next_token["type"] == 'KEYWORD':
            self.parse_characters()
            next_token = self.check_next_token()

    def parse_characters(self):

        next_token = self.check_next_token()
        if next_token is None or next_token["value"] not in [e.value for e in Keyword]:
            print("Incorrect input")
            return

        self.shift_and_match()
        value = next_token["value"]

        if value in ['fd', 'bk', 'rt', 'lt']:
            if self.shift_matching_numeric() is False:
                return
            current_token_value = self.get_current_token()["value"]
            if value == 'fd':
                self.turtle.move_forward(int(current_token_value))
            elif value == 'bk':
                self.turtle.move_backward(int(current_token_value))
            elif value == 'lt':
                self.turtle.rotate(int(current_token_value))
            else:
                self.turtle.rotate(int(-1 * int(current_token_value)))

        if value in ['pu', 'pd', 'ht', 'st']:

            if value == 'pu':
                self.turtle.pen_up()
            elif value == 'pd':
                self.turtle.pen_down()
            elif value == 'st':
                self.turtle.show_turtle()
            else:
                self.turtle.hide_turtle()

        if value == 'repeat':
            if self.shift_matching_numeric() is False:
                return

            times = int(self.get_current_token()["value"])

            if self.shift_and_match('[') is False:
                return

            go_back_and_repeat_index = self.index
            for i in range(0, times):
                self.init_parser()
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
        self.index += 1
        token = self.get_current_token()
        if not token["value"].isnumeric():
            print("Parsing Error: Expected NUMBER but received: " + token["type"])
            return False
        else:
            return True

    def shift_and_match(self, expected_token_type=None):
        self.index += 1
        token = self.get_current_token()
        if expected_token_type is None:
            return True
        if token["type"] != expected_token_type:
            print("Parsing Error: Expected: " + expected_token_type + " but received: " + token["type"])
            return False

    def logo_init(self):
        pygame.init()
        self.turtle = Turtle()
        self.turtle.draw()
        pygame.display.flip()
        pygame.display.set_caption("Logo Interpreter")