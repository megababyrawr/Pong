import pygame
import random
import math
BLACK = (0, 0, 0)
class Ball(pygame.sprite.Sprite):
    #constructor for ball object
    def __init__(self, width, height, colour):
        #sprite constructor
        super().__init__()

        #creats sprite image and draws ellipse on that surface (image)
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.ellipse(self.image, colour, [0, 0, width, height])

        #chooses velocity by randomly choosing a radian between pi/5 and 4pi/5 and 50/50 chance of left or right
        radian = random.uniform(math.pi / 4, -math.pi / 4)
        direction = random.uniform(0, 1)
        if direction > 0.5:
            direction = 1
        else:
            direction = -1
        radian = radian * direction
        xVelocity = math.ceil(math.cos(radian)) + 1
        yVelocity = math.ceil(math.sin(radian)) + 1
        self.velocity = [xVelocity, yVelocity]

        #assigns rect attribute of the image to the sprite rect attribute
        self.rect = self.image.get_rect()

    def update(self):
        #updates rect of sprite with velocity values, this function is called by updating the sprite group
        self.rect.x = self.rect.x + self.velocity[0]
        self.rect.y = self.rect.y + self.velocity[1]

    def hitEdge(self):
        #if hit edge, y velocity switches signs
        self.velocity[1] = self.velocity[1] * -1

    def hitPaddle(self):
        #if hits tab, switch sign of x velocity
        self.velocity[0] = self.velocity[0] * -1

