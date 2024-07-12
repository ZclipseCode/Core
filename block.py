import pygame
# import tile

class Block:
    def __init__(self, screen, tile):
        self.screen = screen
        self.tile = tile
        self.block_sprite = pygame.image.load('Assets/Tetrominoes/Tetromino_block1_1.png')
        self.block_sprite = pygame.transform.scale(self.block_sprite, (16, 16))

    def update(self):
        self.display()

    def display(self):
        self.screen.blit(self.block_sprite, (self.tile.x, self.tile.y))