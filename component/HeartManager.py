import pygame.sprite

import component.Block


class HeartManager(pygame.sprite.Sprite):
    def __init__(self, image, position_first, num, screensize):
        self.set_of_life_player_1 = pygame.sprite.Group()
        self.set_of_life_player_2 = pygame.sprite.Group()
        self.heart_image = image
        self.position_first = position_first
        self.player_1_heart = num
        self.player_2_heart = num
        self.screensize = screensize
        self._create_heart(num)

    def _create_heart(self, num):
        position = list(self.position_first)
        for _ in range(0, num):
            self.set_of_life_player_2.add(component.Block.Block(self.heart_image, position))
            self.set_of_life_player_1.add(
                component.Block.Block(self.heart_image, (self.screensize[0] - position[0],
                                                         self.screensize[1] - position[1])))
            position[0] += 35

    def draw(self, surface):
        self.set_of_life_player_1.draw(surface)
        self.set_of_life_player_2.draw(surface)

    def update(self, player1_heart, player2_heart):
        if player1_heart - self.player_1_heart < 0:
            self.set_of_life_player_1.sprites()[-1].kill()
            self.player_1_heart -= 1
        if player2_heart - self.player_2_heart < 0:
            self.set_of_life_player_2.sprites()[-1].kill()
            self.player_2_heart -= 1
