import pygame
class Ball:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 0

    def display(self, window):
        pygame.draw.circle(window, self.colour, (400, 600), self.size, self.thickness
                           )