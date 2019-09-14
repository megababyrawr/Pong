import pygame
import math
import random
pygame.init()
from Ball import Ball
from Paddle import Paddle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    #variables
    windowHeight = 800 #height
    windowWidth = 1200 #width
    player1Score = 0
    player2Score = 0
    speedFactor = 1
    paddleHitCount = 1

    #sets window properties
    window = pygame.display.set_mode((windowWidth, windowHeight))
    #displays the black canvas
    pygame.display.set_caption('Pong')

    #creates two paddles with width 10 and height 100
    leftPaddle = Paddle(15, 150, WHITE)
    rightPaddle = Paddle(15, 150, WHITE)

    #sets paddle location
    leftPaddle.rect.x = 100
    leftPaddle.rect.y = 400
    rightPaddle.rect.x = 1100
    rightPaddle.rect.y = 400

    puck1 = Ball(25, 25, WHITE)
    puck1.rect.x = 600
    puck1.rect.y = 400

    #creates sprite group and adds all sprites
    allSprites = pygame.sprite.Group()
    allSprites.add(leftPaddle)
    allSprites.add(rightPaddle)
    allSprites.add(puck1)

    clock = pygame.time.Clock()

    running = True  # determines if program keeps running
    #this is the main loop to run game functions
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #to check if user closed
                running = False

        #user key eventhandler W and S for left paddle, up and down for right paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            leftPaddle.up(10)
        if keys[pygame.K_s]:
            leftPaddle.down(10)
        if keys[pygame.K_UP]:
            rightPaddle.up(10)
        if keys[pygame.K_DOWN]:
            rightPaddle.down(10)

        #updates sprites location
        allSprites.update()

        #checks for collision conditions of ball with paddle or edges
        #if puck hits right or left edges
        #right scores
        if puck1.rect.x <= 0:
            player2Score += 1
            puck1.rect.x = 600
            puck1.rect.y = 400
            paddleHitCount = 1
            # calculates new starting velocity
            radian = random.uniform(math.pi / 4, -math.pi / 4)
            direction = random.uniform(0, 1)
            if direction > 0.5:
                direction = 1
            else:
                direction = -1
            radian = radian * direction
            xVelocity = math.ceil(math.cos(radian)) + 1
            yVelocity = math.ceil(math.sin(radian)) + 1
            puck1.velocity = [xVelocity, yVelocity]

        #left scores
        if puck1.rect.x >= 1200:
            player1Score += 1
            puck1.rect.x = 600
            puck1.rect.y = 400
            paddleHitCount = 1
            #calculates new starting velocity
            radian = random.uniform(math.pi / 4, -math.pi / 4)
            direction = random.uniform(0, 1)
            if direction > 0.5:
                direction = 1
            else:
                direction = -1
            radian = radian * direction
            xVelocity = math.ceil(math.cos(radian)) + 1
            yVelocity = math.ceil(math.sin(radian)) + 1
            puck1.velocity = [xVelocity, yVelocity]



        #if puck hits top or bot edges
        if puck1.rect.y <= 0:
            puck1.hitEdge()
        if puck1.rect.y >= 780:
            puck1.hitEdge()

        #if puck hits paddles
        if pygame.sprite.collide_mask(puck1, leftPaddle) or pygame.sprite.collide_mask(puck1, rightPaddle):
            puck1.hitPaddle()
            paddleHitCount += 1
            #this will increase the velocity
            speedFactor = (2 + math.log(paddleHitCount, 10)) / 2
            print(str(speedFactor))
            puck1.velocity[0] = math.ceil(puck1.velocity[0] * speedFactor)
            puck1.velocity[1] = math.ceil(puck1.velocity[1] * speedFactor)

        #drawing loop code
        window.fill(BLACK)
        allSprites.draw(window)

        font = pygame.font.Font(None, 80)
        text1 = font.render(str(player1Score), 1, WHITE)
        window.blit(text1, (200, 20))
        text2 = font.render(str(player2Score), 1, WHITE)
        window.blit(text2, (960, 20))

        #updates window with newly drawn stuff
        pygame.display.flip()
        print(str(puck1.velocity))
        clock.tick(120)

if __name__ == "__main__":
    main()