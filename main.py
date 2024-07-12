import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
delta_time = 0
keys = pygame.key.get_pressed()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # delta time in seconds since last frame, used for framerate-
    # independent physics.
    delta_time = clock.tick(60) / 1000

pygame.quit()