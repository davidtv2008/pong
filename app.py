import pygame
from ball import Ball
from paddle import Paddle
import gameFunction as gf
from score import Score
from button import Button
from settings import Settings


def app():
    
    # initialize pygame
    pygame.mixer.pre_init(22050, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('resources/sound/hit.mp3')

    #create and open a window on the screen with given dimensions
    screen = pygame.display.set_mode((900,600))
    screenRect = screen.get_rect()
    screen.fill((230,230,230))
    pygame.display.set_caption("Pong")

    #make the play button
    play = Button(screen, "Play")

    text_color = (255,255,255)
    button_color = (39, 160, 205)
    font = pygame.font.SysFont(None, 60)
    center = screenRect.center
        
    msg_image = font.render("HELLO WORLD",True,text_color,button_color)
    msg_image_rect = msg_image.get_rect()
    msg_image_rect.center = center

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
        screen.blit(msg_image, msg_image_rect)
        gf.updateScreen(ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6,score,play,setting)
        #pygame.display.flip()
app()
