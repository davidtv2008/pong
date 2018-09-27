import pygame
import sys
from pygame.sprite import Sprite
from settings import Settings

class Paddle(Sprite):
    def __init__(self,screen,player):
        super(Paddle,self).__init__()
        self.screen = screen
        
        self.image = pygame.image.load('resources/images/paddle.gif')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()
        
        #Start each new paddle at the bottom center of the screen.
        if player == 1:
            self.rect.centerx = self.screenRect.left + 60
            self.rect.centery = self.screenRect.centery
        elif player == 2:
            self.rect.centerx = self.screenRect.right - 60
            self.rect.centery = self.screenRect.centery
        elif player ==3:
            self.rect.centerx = self.screenRect.right - 100
            self.rect.centery = self.screenRect.centery
        elif player ==4:
            self.rect.centerx = self.screenRect.right - 140
            self.rect.centery = self.screenRect.centery
        
        #Store a decimal value for the paddle center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
                
        self.movingUp = False
        self.movingDown = False
        self.movingRight = False
        self.movingLeft = False
        self.moving = False

        self.previousy = 0
        self.previousx = 0
        self.previousMoving = False

        self.y = [0,1,2,3,4,5,6,7,8]
        
        self.settings = Settings

    def update(self):
        #player key events
        if self.movingUp and self.rect.top > self.screenRect.top:
            self.centery -= self.settings.paddleSpeed
                
        if self.movingDown and self.rect.bottom < self.screenRect.bottom:
            self.centery += self.settings.paddleSpeed

        self.rect.centery = self.centery
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
       
        
        
    
    def centerShip(self):
        self.center = self.screenRect.centerx