import pygame

import component.Block
import component.Box


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

    def box_initialize(self, boxIMG, animation_hander_box):
        positions_list = [(150, 80), (210, 80), (330, 80), (510, 80), (570, 80),
                          (210,140),(450,140),(570,140),
                          (150, 200), (270, 200), (330, 200), (450, 200), (630, 200),
                          (90, 260), (210, 260), (450, 260), (690, 260),
                          (90,320), (270,320),(330,320), (510,320),(570,320), (690,320),
                          (210,380), (450,380),(570,380),
                          (150,440),(210,440),(330,440),(450,440),(630,440),(690,440),
                          (90,500),(330,500),(570,500),
                          (90,560),(210,560),(390,560),(510,560),(570,560)]
        for position in positions_list:
            self.set_of_box.add(component.Box.Box(boxIMG, position, animation_hander_box))

    def draw(self, surface):
        self.set_of_block.draw(surface)
        self.set_of_box.draw(surface)
