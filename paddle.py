import pygame
import sys
from pygame.sprite import Sprite
from settings import Settings

class Paddle(Sprite):
    def __init__(self,screen,player):
        super(Paddle,self).__init__()
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.player = player

        self.startLine = (self.screenRect.centerx,0)
        self.endLine = (self.screenRect.centerx,self.screenRect.bottom)
    
        

        
        #Start each new paddle at the bottom center of the screen.
        if player == 1:
            self.image = pygame.image.load('resources/images/paddle.gif')
            self.rect = self.image.get_rect()
            self.screenRect = screen.get_rect()
            self.rect.centerx = self.screenRect.left + 60
            self.rect.centery = self.screenRect.centery
            
        elif player == 2:
            self.image = pygame.image.load('resources/images/paddle.gif')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screenRect.right - 60
            self.rect.centery = self.screenRect.centery
            
        elif player ==3:
            self.image = pygame.image.load('resources/images/paddle2.gif')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screenRect.left + 116
            self.rect.centery = self.screenRect.top + 16
        elif player ==4:
            self.image = pygame.image.load('resources/images/paddle2.gif')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screenRect.left +116
            self.rect.centery = self.screenRect.bottom - 16
        elif player ==5:
            self.image = pygame.image.load('resources/images/paddle2.gif')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screenRect.right - 116
            self.rect.centery = self.screenRect.top + 16
        elif player ==6:
            self.image = pygame.image.load('resources/images/paddle2.gif')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screenRect.right - 116
            self.rect.centery = self.screenRect.bottom - 16
            
        
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
            if self.player == 1 or self.player == 3 or self.player == 4:
                self.centery -= 0.5
            else:
                self.centery -= self.settings.paddleSpeed
                
        if self.movingDown and self.rect.bottom < self.screenRect.bottom:
            if self.player == 1 or self.player == 3 or self.player == 4:
                self.centery += 0.5
            else:
                self.centery += self.settings.paddleSpeed

        if (self.player == 3 or self.player == 4) and self.movingRight and self.rect.right < self.screenRect.centerx:
            self.centerx += 0.5

        if (self.player == 3 or self.player == 4) and self.movingLeft and self.rect.left > self.screenRect.left:
            self.centerx -= 0.5
        
        if (self.player == 5 or self.player == 6) and self.movingRight and self.rect.right < self.screenRect.right:
            self.centerx += self.settings.paddleSpeed

        if (self.player == 5 or self.player == 6) and self.movingLeft and self.rect.left > self.screenRect.centerx:
            self.centerx -= self.settings.paddleSpeed
        

        
        self.rect.centery = self.centery
        self.rect.centerx = self.centerx
    
    def blitme(self):
        pygame.draw.line(self.screen,(0,0,0),self.startLine,self.endLine,5)
        self.screen.blit(self.image,self.rect)
        
    
    def centerShip(self):
        self.center = self.screenRect.centerx