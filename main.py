# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") # type: ignore
    print(f"Screen height: {SCREEN_HEIGHT }") # type: ignore

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()