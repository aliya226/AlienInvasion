"""Alien Invasion class"""
import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:

    """Overall class to manage games asset and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #set backround color
        self.bg_color = (230,230,230)

    def run_game(self):

        """Main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #redraw the screen during each loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
                #Make most recent screen visible
            pygame.display.flip()

if __name__ == '__main__':
    AI = AlienInvasion()
    AI.run_game()
