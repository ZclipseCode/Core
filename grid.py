import pygame
import tile
import piece
import random

class Grid:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.tiles = {} # dictionary
        tile_x = 0
        tile_y = 0
        for i in range(int(self.x / 16)):
            for j in range(int(self.x / 16)):
                self.tiles[(tile_x / 16, tile_y / 16)] = tile.Tile(self.screen, tile_x, tile_y)
                tile_x += 16
            tile_x = 0
            tile_y += 16
        
        # pieces
        self.pieces = []

        # core
        core = piece.Piece(self.screen, 'core', self.tiles[(19, 19)])
        core.selected = False
        self.pieces.append(core)

        # first piece
        shapes = ['o', 'i', 's', 'z', 'l', 'j', 't']
        shape_index = random.randint(0, len(shapes) - 1)
        current_piece = piece.Piece(self.screen, shapes[shape_index], self.tiles[(0, 0)])
        self.pieces.append(current_piece)
    
    def update(self, events):
        for p in self.pieces:
            p.update(events)

    def display_rect_tiles(self):
        tile_color_index = 0
        for (x, y), tile in self.tiles.items():
            if tile_color_index == 0:
                tile.display("white")
            elif tile_color_index == 1:
                tile.display("gray")
            elif tile_color_index == 2:
                tile.display("black")

            if tile_color_index == 2:
                tile_color_index = 0
            else:
                tile_color_index += 1
        
        self.tiles[(19, 19)].display("blue")
        self.tiles[(20, 19)].display("blue")
        self.tiles[(19, 20)].display("blue")
        self.tiles[(20, 20)].display("blue")
    
    def click_tile_coordinates(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for (x, y), tile in self.tiles.items():
                    if tile.rect.collidepoint(mouse_pos):
                        print(f"Tile at {tile.rect.topleft} was clicked")