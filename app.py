import pygame
from pygame import Rect
import sys
from ball import Ball
from paddle import Paddle
import gameFunction as gf
from score import Score
from button import Button
from settings import Settings


def app():
    # initialize pygame
    pygame.init()

    #create and open a window on the screen with given dimensions
    screen = pygame.display.set_mode((900,600))
    screenRect = screen.get_rect()
    screen.fill((230,230,230))
    pygame.display.set_caption("Pong")

    #make the play button
    play = Button(screen, "Play")

    setting = Settings()
    setting.gameActive = False
    
    #create my paddles
    paddle1 = Paddle(screen,1)
    paddle2 = Paddle(screen,2)
    paddle3 = Paddle(screen,3)
    paddle4 = Paddle(screen,4)
    paddle5 = Paddle(screen,5)
    paddle6 = Paddle(screen,6)

    ball = Ball(screen)

    score = Score(screen)

    #start the main loop for the game.
    while True:
        gf.checkEvents(ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6,play,setting)
        if setting.gameActive:
            paddle1.update()
            paddle2.update()
            paddle3.update()
            paddle4.update()
            paddle5.update()
            paddle6.update()
            ball.update(paddle1,paddle2,paddle3,paddle4,paddle5,paddle6,score)
        gf.updateScreen(ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6,score,play,setting)
        #pygame.display.flip()
app()
