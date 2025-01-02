# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for member in updatable:
            member.update(dt)
        screen.fill("black")
        for member in drawable:
            member.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000
        x = SCREEN_WIDTH / 1
        y = SCREEN_HEIGHT / 1



if __name__ == "__main__":
    main()

