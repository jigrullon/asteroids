import pygame
import sys
from constants import *
from player import *
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)
    
    player = Player(x,y)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,"black") 
        for elem in drawable:
            elem.draw(screen)
        for elem in updatable:
            elem.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player) == True:
                sys.exit("Game over!")
        pygame.display.flip()
        dt = clock.tick(60) / 1000    



if __name__ == "__main__":
    main()
