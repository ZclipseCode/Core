import block
import pygame

class Piece:
    def __init__(self, screen, shape, tile):
        self.screen = screen
        self.piece = None
        if shape == 'o':
            self.piece = self.o_shape(tile)
        elif shape == 'i':
            self.piece = self.i_shape(tile)
        elif shape == 's':
            self.piece = self.s_shape(tile)
        elif shape == 'z':
            self.piece = self.z_shape(tile)
        elif shape == 'l':
            self.piece = self.l_shape(tile)
        elif shape == 'j':
            self.piece = self.j_shape(tile)
        elif shape == 't':
            self.piece = self.t_shape(tile)
    
    def update(self):
        for block in self.piece:
            block.update()

    def o_shape(self, tile):
        o = []
        o.append(block.Block(self.screen, 'white', tile))
        o.append(block.Block(self.screen, 'white', pygame.math.Vector2(tile.x + 16, tile.y)))
        o.append(block.Block(self.screen, 'white', pygame.math.Vector2(tile.x, tile.y + 16)))
        o.append(block.Block(self.screen, 'white', pygame.math.Vector2(tile.x + 16, tile.y + 16)))
        return o
    
    def i_shape(self, tile):
        i = []
        i.append(block.Block(self.screen, 'pink', tile))
        i.append(block.Block(self.screen, 'pink', pygame.math.Vector2(tile.x, tile.y + 16)))
        i.append(block.Block(self.screen, 'pink', pygame.math.Vector2(tile.x, tile.y + 32)))
        i.append(block.Block(self.screen, 'pink', pygame.math.Vector2(tile.x, tile.y + 48)))
        return i
    
    def s_shape(self, tile):
        s = []
        s.append(block.Block(self.screen, 'gray', tile))
        s.append(block.Block(self.screen, 'gray', pygame.math.Vector2(tile.x + 16, tile.y)))
        s.append(block.Block(self.screen, 'gray', pygame.math.Vector2(tile.x + 16, tile.y - 16)))
        s.append(block.Block(self.screen, 'gray', pygame.math.Vector2(tile.x + 32, tile.y - 16)))
        return s
    
    def z_shape(self, tile):
        z = []
        z.append(block.Block(self.screen, 'purple', tile))
        z.append(block.Block(self.screen, 'purple', pygame.math.Vector2(tile.x + 16, tile.y)))
        z.append(block.Block(self.screen, 'purple', pygame.math.Vector2(tile.x + 16, tile.y + 16)))
        z.append(block.Block(self.screen, 'purple', pygame.math.Vector2(tile.x + 32, tile.y + 16)))
        return z
    
    def l_shape(self, tile):
        l = []
        l.append(block.Block(self.screen, 'blue', tile))
        l.append(block.Block(self.screen, 'blue', pygame.math.Vector2(tile.x, tile.y + 16)))
        l.append(block.Block(self.screen, 'blue', pygame.math.Vector2(tile.x, tile.y + 32)))
        l.append(block.Block(self.screen, 'blue', pygame.math.Vector2(tile.x + 16, tile.y + 32)))
        return l
    
    def j_shape(self, tile):
        j = []
        j.append(block.Block(self.screen, 'green', tile))
        j.append(block.Block(self.screen, 'green', pygame.math.Vector2(tile.x, tile.y + 16)))
        j.append(block.Block(self.screen, 'green', pygame.math.Vector2(tile.x, tile.y + 32)))
        j.append(block.Block(self.screen, 'green', pygame.math.Vector2(tile.x - 16, tile.y + 32)))
        return j
    
    def t_shape(self, tile):
        t = []
        t.append(block.Block(self.screen, 'orange', tile))
        t.append(block.Block(self.screen, 'orange', pygame.math.Vector2(tile.x + 16, tile.y)))
        t.append(block.Block(self.screen, 'orange', pygame.math.Vector2(tile.x + 32, tile.y)))
        t.append(block.Block(self.screen, 'orange', pygame.math.Vector2(tile.x + 16, tile.y + 16)))
        return t