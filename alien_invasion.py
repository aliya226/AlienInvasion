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
            self._check_events()
            self.ship_update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #Move the ship to the right
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                #Move the ship up
                if event.type == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        #redraw the screen during each loop
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        #Make most recent screen visible
        pygame.display.flip()

if __name__ == '__main__':
    AI = AlienInvasion()
    AI.run_game()
