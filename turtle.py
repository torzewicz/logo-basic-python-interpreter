import pygame
import math

WINDOWX = 500
WINDOWY = 500

# TURTLE PROPERTIES
TURTLE_WIDTH = 25
TURTLE_HEIGHT = 25


class Turtle:

    def __init__(self, mainx, mainy):
        self.x = mainx / 2
        self.y = mainy / 2
        self.angle = 90
        self.angleRad = math.radians(self.angle)
        self.pointStart = []
        self.pointEnd = []
        self.lineColor = []
        self.isPenUp = False
        self.isVisible = True
        self.penColor = (0, 0, 0)
        self.setImage(pygame.image.load("turtle.png"))

    def hideTurtle(self):
        self.isVisible = False

    def showTurtle(self):
        self.isVisible = True

    def penUp(self):
        self.isPenUp = True

    def penDown(self):
        self.isPenUp = False

    def setPenColor(self, red, green, blue):
        # print red + green + blue
        self.penColor = (red, green, blue)

    def draw(self, screen):
        if self.isVisible:
            screen.blit(self.image, self.imageRect)
        if self.pointStart is not None:
            for px, py, pc in zip(self.pointStart, self.pointEnd, self.lineColor):
                pygame.draw.line(screen, pc, px, py, 2)

    def setImage(self, image):
        self.image = image
        self.imageSave = self.image
        self.imageRect = image.get_rect()
        self.imageRect = self.imageRect.move([self.x, self.y])
        self.x = self.imageRect.centerx
        self.y = self.imageRect.centery

    def rotate(self, angle):
        self.angle += angle
        self.angleRad = math.radians(self.angle)
        self.image = rot_center(self.imageSave, self.image, self.angle)

    def mvForward(self, distance, screen):
        if self.isPenUp == False:
            self.pointStart.append((self.x, self.y))
            self.lineColor.append(self.penColor)

        self.imageRect = self.imageRect.move(
            [int(distance * math.cos(self.angleRad)), int(-distance * math.sin(self.angleRad))])
        self.x = self.imageRect.centerx
        self.y = self.imageRect.centery

        if self.isPenUp == False:
            self.pointEnd.append((self.x, self.y))

    # print self.imageRect
    def mvBackward(self, distance, screen):
        if self.isPenUp == False:
            self.pointStart.append((self.x, self.y))
            self.lineColor.append(self.penColor)

        self.imageRect = self.imageRect.move(
            [-int(distance * math.cos(self.angleRad)), int(distance * math.sin(self.angleRad))])
        self.x = self.imageRect.centerx
        self.y = self.imageRect.centery

        if self.isPenUp == False:
            self.pointEnd.append((self.x, self.y))


def rot_center(orig_image, image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(orig_image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
