import sys

import pygame

class AlienInvasion:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("SPACE MONSTER HOORAY")

    def run_game(self):
        """Start main game loop"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

