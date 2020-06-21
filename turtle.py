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
        self.point_start = []
        self.point_end = []
        self.line_color = []
        self.is_pen_up = False
        self.is_visible = True
        self.screen = pygame.display.set_mode((window_x, window_y))
        self.image = None
        self.imageRect = None
        self.set_turtle_image(pygame.image.load("turtle.png"))

    def hide_turtle(self):
        self.is_visible = False

    def show_turtle(self):
        self.is_visible = True

    def pen_up(self):
        self.is_pen_up = True

    def pen_down(self):
        self.is_pen_up = False

    def draw(self):
        self.screen.fill(background_color)
        if self.is_visible:
            self.screen.blit(self.image, self.imageRect)
        if self.point_start is not None:
            for px, py, pc in zip(self.point_start, self.point_end, self.line_color):
                pygame.draw.line(self.screen, pc, px, py, 2)

    def set_turtle_image(self, image):

        self.image = image
        self.imageRect = image.get_rect()
        self.imageRect = self.imageRect.move([self.x, self.y])
        self.x = self.imageRect.centerx
        self.y = self.imageRect.centery

    def rotate(self, angle):
        self.angle += angle
        self.angle_radians = math.radians(self.angle)

    def mv_forward(self, distance):

        if self.is_pen_up is False:
            self.point_start.append((self.x, self.y))
            self.line_color.append((0, 0, 0))

        self.imageRect = self.imageRect.move(
            [int(distance * math.cos(self.angle_radians)), int(-distance * math.sin(self.angle_radians))])
        self.x = self.imageRect.centerx
        self.y = self.imageRect.centery

        if self.is_pen_up is False:
            self.point_end.append((self.x, self.y))

    def move_backward(self, distance):

        if self.is_pen_up is False:
            self.point_start.append((self.x, self.y))
            self.line_color.append((0, 0, 0))

        self.imageRect = self.imageRect.move(
            [-int(distance * math.cos(self.angle_radians)), int(distance * math.sin(self.angle_radians))])
        self.x = self.imageRect.centerx
        self.y = self.imageRect.centery

        if self.is_pen_up is False:
            self.point_end.append((self.x, self.y))
