# this allows us to use code from
# the open-source pygame library
# throughout this file
import time
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
import pygame
from player import Player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") # type: ignore
    print(f"Screen height: {SCREEN_HEIGHT }") # type: ignore

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pygame.time.Clock()

    updatable  = pygame.sprite.Group()
    drawable   = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots      = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots,updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if player.collisions(obj):
                print("Game over!")
                return

            for bullet in shots:
                if obj.collisions(bullet):
                    print("boomm!")
                    obj.split()
                    bullet.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()