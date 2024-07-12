import pygame

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
                self.tiles[(tile_x / 16, tile_y / 16)] = Tile(self.screen, tile_x, tile_y)
                tile_x += 16
            tile_x = 0
            tile_y += 16
    
    def update(self):
        self.display_rect_tiles()
        # self.click_tile_coordinates()

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

class Tile:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pygame.draw.rect(self.screen, "white", (self.x, self.y, 16, 16))

    def display(self, color):
        # color can be a string (ex: "white")
        pygame.draw.rect(self.screen, color, (self.x, self.y, 16, 16))