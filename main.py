# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    fps = 60
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()  # This should be created early in your game
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid_group)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)


    # Create player in middle of the screen and add player to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroid_field = AsteroidField()

    while True:  # This creates an infinite loop
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the function, ending the game
       
        #update updatable group with dt
        updatable.update(dt)

        # Iterate over all objects in your asteroids group
        for asteroid in asteroid_group:
            if player.detect_collision(asteroid):  # If a collision is detected
                print("Game over!")
                sys.exit(0)  # End the game immediately

        for asteroid in asteroid_group:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    new_asteroids = asteroid.split()
                
                                    
        # Fill the screen with black
        screen.fill("black")  # Note: we use screen.fill, not pygame.fill

    
        # Draw player group in each frame
        for sprite in drawable:
            sprite.draw(screen)

                       
        # Update the display
        pygame.display.flip()
        dt = clock.tick(fps) / 1000


if __name__ == "__main__":
    main()
