import pygame
import sys

def checkEvents(ball,screen,paddle1,paddle2,paddle3,paddle4):
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event,ball,screen,paddle1,paddle2,paddle3,paddle4)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event,ball,screen,paddle1,paddle2,paddle3,paddle4)


def checkKeyDownEvents(event,ball,screen,paddle1,paddle2,paddle3,paddle4):
    if event.key == pygame.K_UP:
        if ball.movingRight:
            paddle2.movingUp = True
            paddle1.movingUp = False
        elif ball.movingLeft:
            paddle1.movingUp = True
            paddle2.movingUp = False
    elif event.key == pygame.K_DOWN:
        if ball.movingRight:
            paddle2.movingDown = True
            paddle1.movingDown = False
        elif ball.movingLeft:
            paddle1.movingDown = True
            paddle2.movingDown = False
    elif event.key == pygame.K_RIGHT:
        if ball.movingUp or ball.movingDown:
            paddle3.movingRight = True
            paddle4.movingRight = True
            paddle3.movingLeft = False
            paddle4.movingLeft = False
    elif event.key == pygame.K_LEFT:
        if ball.movingUp or ball.movingDown:
            paddle3.movingLeft = True
            paddle4.movingLeft = True
            paddle3.movingRight = False
            paddle4.movingRight = False
    elif event.key == pygame.K_q:
        sys.exit()

def checkKeyUpEvents(event,ball,screen,paddle1,paddle2,paddle3,paddle4):
    if event.key == pygame.K_UP:
        paddle1.movingUp = False
        paddle2.movingUp = False
    elif event.key == pygame.K_DOWN:
        paddle1.movingDown = False
        paddle2.movingDown = False
    
def updateScreen(ball,screen,paddle1,paddle2,paddle3,paddle4,score):
    screen.fill((230,230,230))
    ball.blitme()
    paddle1.blitme()
    paddle2.blitme()
    paddle3.blitme()
    paddle4.blitme()
    score.showScore()
    pygame.display.update()