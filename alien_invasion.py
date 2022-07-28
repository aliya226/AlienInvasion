import sys
import pygame

class AlienInvasion:
    """Overall class to manage games asset and behavior""" 
    
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
        def run_game(self):
            """Main loop for the game"""
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                
                pygame.display.flip()
        