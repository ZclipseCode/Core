import pygame

class Tile:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.draw.rect(self.screen, "white", (self.x, self.y, 16, 16))

    def display(self, color):
        # color can be a string (ex: "white")
        pygame.draw.rect(self.screen, color, (self.x, self.y, 16, 16))