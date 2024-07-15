import pygame

# block controller class?
class Block:
    def __init__(self, screen, color, tile):
        self.screen = screen
        self.tile = tile

        self.block = None

        if color == 'core':
            self.block = pygame.image.load('Assets/Tetrominoes/Tetromino_block2_3.png')
        elif color == 'white':
            self.block = pygame.image.load('Assets/Tetrominoes/Tetromino_block1_1.png')
        elif color == 'pink':
            self.block = pygame.image.load('Assets/Tetrominoes/Tetromino_block1_2.png')
        elif color == 'gray':
            self.block = pygame.image.load('Assets/Tetrominoes/Tetromino_block1_3.png')
        elif color == 'purple':
            self.block = pygame.image.load('Assets/Tetrominoes/Tetromino_block1_4.png')
        elif color == 'blue':
            self.block = pygame.image.load('Assets/Tetrominoes/Tetromino_block1_5.png')
        elif color == 'green':
            self.block = pygame.image.load('Assets/Tetrominoes/Tetromino_block1_6.png')
        elif color == 'orange':
            self.block = pygame.image.load('Assets/Tetrominoes/Tetromino_block1_7.png')
        
        self.block = pygame.transform.scale(self.block, (16, 16))

    def update(self):
        self.display()

    def display(self):
        self.screen.blit(self.block, (self.tile.x, self.tile.y))