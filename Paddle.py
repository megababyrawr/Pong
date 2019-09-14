import pygame

class Paddle(pygame.sprite.Sprite):
    #constructor for paddle obj, parameters are width and height of paddle and colour of paddle
    def __init__(self, width, height, colour):
        #constructs parent object (Sprite)
        super().__init__()

        #creating the paddle's image (sprite attribute) that will be drawn in main
        BLACK = (0, 0, 0)
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draws the paddle as a rectangle onto the image surface, with input colour and with [rectangle] properties
        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        #assigns rect attribute of the image to the sprite rect attribute
        self.rect = self.image.get_rect()

    #two functions for moving paddle up and down
    def up(self, pixels):
        self.rect.y = self.rect.y - pixels
        #if paddle tries to go off screen
        if self.rect.y < 0:
            self.rect.y = 0

    def down(self, pixels):
        self.rect.y = self.rect.y + pixels
        if self.rect.y > 800-130:
            self.rect.y = 800-130



