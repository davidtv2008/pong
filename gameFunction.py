import pygame
import sys

def checkEvents(ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6,play,setting):
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event,ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event,ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(play,mouse_x,mouse_y,setting)
        
def check_play_button(play,mouse_x,mouse_y,setting):
    """Start a new game when the player click Play."""
    button_clicked = play.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and not setting.gameActive:
        print("mouse clicked")        
        #Hide the mouse cursor
        #pygame.mouse.set_visible(False)
        setting.gameActive = True
        print(str(setting.gameActive))
        #reset the game statistics

def checkKeyDownEvents(event,ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6):

    if event.key == pygame.K_UP:
        paddle1.movingUp = True
        paddle2.movingUp = True
    if event.key == pygame.K_DOWN:
        paddle1.movingDown = True
        paddle2.movingDown = True
    if event.key == pygame.K_RIGHT:
        paddle3.movingRight = True
        paddle4.movingRight = True
        paddle5.movingRight = True
        paddle6.movingRight = True
    if event.key == pygame.K_LEFT:
        paddle3.movingLeft = True
        paddle4.movingLeft = True
        paddle5.movingLeft = True
        paddle6.movingLeft = True    
    if event.key == pygame.K_q:
        sys.exit()

def checkKeyUpEvents(event,ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6):
    if event.key == pygame.K_UP:
        paddle1.movingUp = False
        paddle2.movingUp = False
    if event.key == pygame.K_DOWN:
        paddle1.movingDown = False
        paddle2.movingDown = False
    if event.key == pygame.K_RIGHT:
        paddle3.movingRight = False
        paddle4.movingRight = False
        paddle5.movingRight = False
        paddle6.movingRight = False
    if event.key == pygame.K_LEFT:
        paddle3.movingLeft = False
        paddle4.movingLeft = False
        paddle5.movingLeft = False
        paddle6.movingLeft = False
    
def updateScreen(ball,screen,paddle1,paddle2,paddle3,paddle4,paddle5,paddle6,score,play,setting):
    screen.fill((230,230,230))
    ball.blitme()
    paddle1.blitme()
    paddle2.blitme()
    paddle3.blitme()
    paddle4.blitme()
    paddle5.blitme()
    paddle6.blitme()
    score.showScore()
    #pygame.display.update()
    if not setting.gameActive:
        play.draw_button()
    pygame.display.flip()