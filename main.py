# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    while True:  # This creates an infinite loop
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the function, ending the game
        
        # Fill the screen with black
        screen.fill("black")  # Note: we use screen.fill, not pygame.fill
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
