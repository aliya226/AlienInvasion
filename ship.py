"""Ship class"""
import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Inialize the ship and its starting point"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen.rect.midbottom

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1


    def draw_ship(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
