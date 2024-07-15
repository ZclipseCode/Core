import block
import pygame

class Piece:
    def __init__(self, screen, shape, tile):
        self.screen = screen
        self.shape = shape
        self.tile = tile
        self.selected = True
        self.piece = None
        self.movement()
    
    def update(self, events):
        if self.selected:
            self.input(events)

        self.movement()

        for block in self.piece:
            block.update()
    
    def input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.tile.set_xy(self.tile.x, self.tile.y - 16)
                elif event.key == pygame.K_RIGHT:
                    self.tile.set_xy(self.tile.x + 16, self.tile.y)
                elif event.key == pygame.K_DOWN:
                    self.tile.set_xy(self.tile.x, self.tile.y + 16)
                elif event.key == pygame.K_LEFT:
                    self.tile.set_xy(self.tile.x - 16, self.tile.y)

    def movement(self):
        if self.shape == 'core':
            self.piece = self.core_shape(self.tile)
        elif self.shape == 'o':
            self.piece = self.o_shape(self.tile)
        elif self.shape == 'i':
            self.piece = self.i_shape(self.tile)
        elif self.shape == 's':
            self.piece = self.s_shape(self.tile)
        elif self.shape == 'z':
            self.piece = self.z_shape(self.tile)
        elif self.shape == 'l':
            self.piece = self.l_shape(self.tile)
        elif self.shape == 'j':
            self.piece = self.j_shape(self.tile)
        elif self.shape == 't':
            self.piece = self.t_shape(self.tile)

    def core_shape(self, tile):
        core = []
        core.append(block.Block(self.screen, 'core', tile))
        core.append(block.Block(self.screen, 'core', pygame.math.Vector2(tile.x + 16, tile.y)))
        core.append(block.Block(self.screen, 'core', pygame.math.Vector2(tile.x, tile.y + 16)))
        core.append(block.Block(self.screen, 'core', pygame.math.Vector2(tile.x + 16, tile.y + 16)))
        return core        

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