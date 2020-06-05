import os
import pygame
from FractalTree import FractalTree, Point

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"
    pygame.display.init()
    pygame.display.set_caption("Fractal Tree")
    size = Point(650, 650)
    screen = pygame.display.set_mode(size)
    tree = FractalTree(45, 5);
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(0)
        pygame.display.update()


if __name__ == "__main__":
    main()
