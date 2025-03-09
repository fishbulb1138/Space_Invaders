import sys

import pygame

class AlienInvasion:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("SPACE MONSTER HOORAY")
        # set background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main game loop"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw screen through each pass of the loop
            self.screen.fill(self.bg_colorg)

            # make most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

