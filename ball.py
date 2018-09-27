import pygame
import sys
from pygame.sprite import Sprite
from settings import Settings

class Ball(Sprite):
    def __init__(self,screen):
        super(Ball,self).__init__()
        self.screen = screen
        
        self.image = pygame.image.load('resources/images/ball.gif')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()
        
        #Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screenRect.centerx
        self.rect.centery = self.screenRect.centery
        
        #Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.movingRight = False
        self.movingLeft = False
        self.movingUp = True
        self.movingDown = False

        self.previousy = 0
        self.previousx = 0

        self.settings = Settings
        
    def update(self,paddle1,paddle2,paddle3,paddle4,score):

        ball = self.rect

        #store each paddles separate parts in which
        #the ball will bounce differently depending on where it hit
        i = 0
        while i < 9:
            paddle1.y[i] = paddle1.rect.top + (16*i)
            paddle2.y[i] = paddle2.rect.top + (16*i)
            i += 1

        #ball moving down in either direction
        if self.movingDown:
            self.centery += self.settings.ballSpeed

            #ball moving down in the right direction
            if self.previousx < self.centerx:
                self.movingRight = True
                self.movingLeft = False
                self.previousx = self.centerx
                self.centerx += self.settings.ballSpeed

            #ball moving down in the left direction
            elif self.previousx > self.centerx:
                self.movingRight = False
                self.movingLeft = True
                self.previousx = self.centerx
                self.previousy = self.centery
                self.centerx -= self.settings.ballSpeed
            
            #if ball hits bottom window bounce off
            if ball.bottom >= self.screenRect.bottom:
                self.movingDown = False
                self.movingUp = True
            
            #player 2 right side paddle
            #if ball bottom edge is below paddle top, also if ball top edge is above paddle bottom edge, and if they are touching ball right touches paddle left
            #if ball.bottom > paddle2.y[0] and ball.top < paddle2.y[8] and ball.right == paddle2.rect.left:
            if ball.colliderect(paddle2.rect):
                if ball.bottom > paddle2.y[0] and ball.top < paddle2.y[1]:
                    if paddle2.movingUp:
                        self.centery += 0.8
                    elif paddle2.movingDown:
                        self.centery += 1
                    else:
                        self.centery += 0.2
                elif ball.bottom > paddle2.y[1] and ball.top < paddle2.y[2]:
                    if paddle2.movingUp:
                        self.centery += 1
                    elif paddle2.movingDown:
                        self.centery += 1.2
                    else:
                        self.centery += 0.3
                elif ball.bottom > paddle2.y[2] and ball.top < paddle2.y[3]:
                    if paddle2.movingUp:
                        self.centery += 1.4
                    elif paddle2.movingDown:
                        self.centery += 1.6
                    else:
                        self.centery += 0.4
                elif ball.bottom > paddle2.y[3] and ball.top < paddle2.y[4]:
                    if paddle2.movingUp:
                        self.centery += 1.8
                    elif paddle2.movingDown:
                        self.centery += 2
                    else:
                        self.centery += 0.5
                elif ball.bottom > paddle2.y[4] and ball.top < paddle2.y[5]:
                    if paddle2.movingUp:
                        self.centery += 2
                    elif paddle2.movingDown:
                        self.centery += 2.2
                    else:
                        self.centery += 0.6
                elif ball.bottom > paddle2.y[5] and ball.top < paddle2.y[6]:
                    if paddle2.movingUp:
                        self.centery += 2.4
                    elif paddle2.movingDown:
                        self.centery += 2.6
                    else:
                        self.centery += 0.8
                elif ball.bottom > paddle2.y[6] and ball.top < paddle2.y[7]:
                    if paddle2.movingUp:
                        self.centery += 2.6
                    elif paddle2.movingDown:
                        self.centery += 2.8
                    else:
                        self.centery += 0.9
                elif ball.bottom > paddle2.y[7] and ball.top < paddle2.y[8]:
                    if paddle2.movingUp:
                        self.centery += 3.0
                    elif paddle2.movingDown:
                        self.centery += 3.2
                    else:
                        self.centery += 1
                
                self.movingRight = False
                self.movingLeft = True
                self.centerx += -(self.settings.ballSpeed)

                #speed up the ball after each paddle strikes
                self.settings.ballSpeed += 0.01
            
            #player 1
            #if ball bottom edge is below paddle top, also if ball top edge is above paddle bottom edge, and if they are touching ball left touches paddle right
            if ball.colliderect(paddle1.rect):  
                
                if ball.bottom > paddle1.y[0] and ball.top < paddle1.y[1]:
                    self.centery += 0.2
                elif ball.bottom > paddle1.y[1] and ball.top < paddle1.y[2]:
                    self.centery += 0.3
                elif ball.bottom > paddle1.y[2] and ball.top < paddle1.y[3]:
                    self.centery += 0.4
                elif ball.bottom > paddle1.y[3] and ball.top < paddle1.y[4]:
                    self.centery += 0.5
                elif ball.bottom > paddle1.y[4] and ball.top < paddle1.y[5]:
                    self.centery += 0.6
                elif ball.bottom > paddle1.y[5] and ball.top < paddle1.y[6]:
                    self.centery += 0.8
                elif ball.bottom > paddle1.y[6] and ball.top < paddle1.y[7]:
                    self.centery += 0.9
                elif ball.bottom > paddle1.y[7] and ball.top < paddle1.y[8]:
                    self.centery += 1

                self.movingRight = True
                self.movingLeft = False
                self.centerx += self.settings.ballSpeed

                #speed up ball after each strike
                self.settings.ballSpeed += 0.01

        #ball moving up in either direction
        if self.movingUp:
            self.centery -= self.settings.ballSpeed

            #ball moving in the right direction            
            if self.previousx < self.centerx:
                self.movingRight = True
                self.movingLeft = False
                self.previousx = self.centerx
                self.previousy = self.centery
                self.centerx += self.settings.ballSpeed
            
            #ball moving in the left direction
            elif self.previousx > self.centerx:
                self.movingRight = False
                self.movingLeft = True
                self.previousx = self.centerx
                self.previousy = self.centery
                self.centerx -= self.settings.ballSpeed

            #if ball hits top window edge bounce
            if ball.top <= self.screenRect.top:
                self.movingUp = False
                self.movingDown = True

            #player2 right side paddle
            #if ball bottom is bellow paddle top, and ball top is above paddle bottom, and ball right side is touching paddle left side 
            if ball.colliderect(paddle2.rect):

                if ball.bottom > paddle2.y[0] and ball.top < paddle2.y[1]:
                    self.centery += 0.2
                elif ball.bottom > paddle2.y[1] and ball.top < paddle2.y[2]:
                    self.centery += 0.3
                elif ball.bottom > paddle2.y[2] and ball.top < paddle2.y[3]:
                    self.centery += 0.4
                elif ball.bottom > paddle2.y[3] and ball.top < paddle2.y[4]:
                    self.centery += 0.5
                elif ball.bottom > paddle2.y[4] and ball.top < paddle2.y[5]:
                    self.centery += 0.6
                elif ball.bottom > paddle2.y[5] and ball.top < paddle2.y[6]:
                    self.centery += 0.8
                elif ball.bottom > paddle2.y[6] and ball.top < paddle2.y[7]:
                    self.centery += 0.9
                elif ball.bottom > paddle2.y[7] and ball.top < paddle2.y[8]:
                    self.centery += 1

                self.movingRight = False
                self.movingLeft = True
                self.centerx += -(self.settings.ballSpeed)

                #speed up ball after each strike
                self.settings.ballSpeed += 0.01

            #player 1 left side paddle
            #check if there is a collision between ball and paddle rect
            if ball.colliderect(paddle1.rect):
                
                if ball.bottom > paddle1.y[0] and ball.top < paddle1.y[1]:
                    self.centery += 0.2
                elif ball.bottom > paddle1.y[1] and ball.top < paddle1.y[2]:
                    self.centery += 0.3
                elif ball.bottom > paddle1.y[2] and ball.top < paddle1.y[3]:
                    self.centery += 0.4
                elif ball.bottom > paddle1.y[3] and ball.top < paddle1.y[4]:
                    self.centery += 0.5
                elif ball.bottom > paddle1.y[4] and ball.top < paddle1.y[5]:
                    self.centery += 0.6
                elif ball.bottom > paddle1.y[5] and ball.top < paddle1.y[6]:
                    self.centery += 0.8
                elif ball.bottom > paddle1.y[6] and ball.top < paddle1.y[7]:
                    self.centery += 0.9
                elif ball.bottom > paddle1.y[7] and ball.top < paddle1.y[8]:
                    self.centery += 1

                self.movingRight = True
                self.movingLeft = False
                self.centerx += self.settings.ballSpeed

                #speed up ball after each strike
                self.settings.ballSpeed += 0.01

        #check if either player has scored
        #if ball hits left or right window
        if ball.left >= self.screenRect.right:
            score.player1Score += 1
            self.settings.ballSpeed = 1.3
            score.prep_score()
            #Start each new ship at the bottom center of the screen.
            self.rect.centerx = self.screenRect.centerx
            self.rect.centery = self.screenRect.centery
            self.centerx = float(self.rect.centerx)
            self.centery = float(self.rect.centery) 
        elif ball.right <= self.screenRect.left:
            score.player2Score += 1
            self.settings.ballSpeed = 1.3
            score.prep_score()
            #Start each new ship at the bottom center of the screen.
            self.rect.centerx = self.screenRect.centerx
            self.rect.centery = self.screenRect.centery
            self.centerx = float(self.rect.centerx)
            self.centery = float(self.rect.centery)

        #new ball position
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def centerShip(self):
        self.center = self.screenRect.centerx

            
    