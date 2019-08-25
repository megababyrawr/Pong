import pygame
from Ball import Ball

def main():
    #variables
    windowHeight = 800 #height
    windowWidth = 1200 #width

    puck1 = Ball(400, 600, 10)
    #sets window properties
    window = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Pong')
    puck1.display(window)

    #updates display
    pygame.display.flip()


    running = True  # determines if program keeps running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()