import pygame

class Background:
    def __init__(self, screen):
        self.screen = screen
        self.background_tile = pygame.image.load('Assets/Tetrominoes/Pattern01.png')

    def update(self):
        rows = 5
        columns = 5
        x = 0
        y = 0
        for i in range(rows):
            for j in range(columns):
                self.screen.blit(self.background_tile, (x,y))
                x += 128
            x = 0
            y += 128