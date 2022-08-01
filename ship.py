"""Ship class"""
import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self,ai_game):
        """Inialize the ship and its starting point"""
        self.moving_right = False
        self.moving_left = False
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

            #Update rect object
            self.rect.x = self.x


    def draw_ship(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
