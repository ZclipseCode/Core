import pygame
import background
import grid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True
delta_time = 0
keys = pygame.key.get_pressed()

_background = background.Background(screen)
_grid = grid.Grid(screen, 640, 640)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # fill the screen with a color to wipe away anything from last frame
    # is this needed?
    screen.fill("grey")

    _background.update()
    _grid.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # delta time in seconds since last frame, used for framerate-
    # independent physics.
    delta_time = clock.tick(60) / 1000

pygame.quit()