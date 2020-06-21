import pygame
import math

background_color = (169, 169, 169)

window_x = 600
window_y = 600


class Turtle:

    def __init__(self):
        self.x = window_x / 2
        self.y = window_y / 2
        self.angle = 90
        self.angle_radians = math.radians(self.angle)
        self.lines_start_list = []
        self.lines_end_list = []
        self.is_pen_up = False
        self.draw_turtle_object = True
        self.screen = pygame.display.set_mode((window_x, window_y))
        self.image = None
        self.image_rect = None
        self.set_turtle_image(pygame.image.load("turtle.png"))

    def draw(self):
        self.screen.fill(background_color)
        if self.draw_turtle_object:
            self.screen.blit(self.image, self.image_rect)
        if self.lines_start_list is not None:
            for start_point_x, start_point_y in zip(self.lines_start_list, self.lines_end_list):
                pygame.draw.line(self.screen, (0, 0, 0), start_point_x, start_point_y, 2)

    def set_turtle_image(self, image):

        self.image = image
        self.image_rect = image.get_rect()
        self.image_rect = self.image_rect.move([self.x, self.y])
        self.x = self.image_rect.centerx
        self.y = self.image_rect.centery

    def rotate(self, angle):
        self.angle += angle
        self.angle_radians = math.radians(self.angle)

    def move(self, distance, turn):
        if self.is_pen_up is False:
            self.lines_start_list.append((self.x, self.y))

        self.image_rect = self.image_rect.move(
            [turn * int(distance * math.cos(self.angle_radians)),
             int(turn * -distance * math.sin(self.angle_radians))])

        self.x = self.image_rect.centerx
        self.y = self.image_rect.centery

        if self.is_pen_up is False:
            self.lines_end_list.append((self.x, self.y))

    def move_forward(self, distance):
        self.move(distance, 1)

    def move_backward(self, distance):
        self.move(distance, -1)

    def hide_turtle(self):
        self.draw_turtle_object = False

    def show_turtle(self):
        self.draw_turtle_object = True

    def pen_up(self):
        self.is_pen_up = True

    def pen_down(self):
        self.is_pen_up = False