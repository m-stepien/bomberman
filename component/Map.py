import pygame

import component.Block


class Map:
    # 800, 600
    def __init__(self):
        self.set_of_block = pygame.sprite.Group()
        self.set_of_box = pygame.sprite.Group()
        self.set_of_bomb = pygame.sprite.Group()

    def block_initialize(self, blockIMG):
        x, y = 30, 30
        while x < 780:
            self.set_of_block.add(component.Block.Block(blockIMG, (x, y)))
            x += 60
        x = 30
        i = 0
        y += 60
        while y < 660 - 60:
            self.set_of_block.add(component.Block.Block(blockIMG, (x, y)))
            self.set_of_block.add(component.Block.Block(blockIMG, (780 - x, y)))
            if i % 2:
                x += 60 * 2
                while x < 780 - 60:
                    self.set_of_block.add(component.Block.Block(blockIMG, (x, y)))
                    x += 60 * 2

                x = 30
            i += 1
            y += 60
        while x < 780:
            self.set_of_block.add(component.Block.Block(blockIMG, (x, y)))
            x += 60

    def draw(self, surface):
        # TODO: rysowanie pociskow i przeszkod
        self.set_of_block.draw(surface)
