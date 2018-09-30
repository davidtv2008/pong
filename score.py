import pygame.font
from pygame.sprite import Group

class Score():
    """A class to report scoring information."""

    def __init__(self, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 64)

        self.player1Score = 0
        self.player2Score = 0

        # Prepare the initial score images.
        self.prep_score()
        
        

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score1 = self.player1Score
        rounded_score2 = self.player2Score
        score_str1 = "{:,}".format(rounded_score1)
        score_str2 = "{:,}".format(rounded_score2)
        self.score_image1 = self.font.render(score_str1, True, self.text_color,(8,235,46))
        self.score_image2 = self.font.render(score_str2, True, self.text_color,(8,235,46))
            
        # Display the score at the top right of the screen.
        self.score_rect1 = self.score_image1.get_rect()
        self.score_rect2 = self.score_image2.get_rect()
        
        self.score_rect1.right = self.screen_rect.centerx +80
        self.score_rect2.left = self.screen_rect.centerx - 80

        self.score_rect1.top = 30
        self.score_rect2.top = 30
            
    def showScore(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image1, self.score_rect1)
        self.screen.blit(self.score_image2,self.score_rect2)
        