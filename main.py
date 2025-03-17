import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")
        pygame.display.flip()

        # Limit framerate to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
