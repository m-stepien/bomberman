import pygame

import component.Block
import component.Box
import component.Explosion


class Map:
    def __init__(self):
        self.set_of_block = pygame.sprite.Group()
        self.set_of_box = pygame.sprite.Group()
        self.set_of_bomb = pygame.sprite.Group()
        self.set_of_explosion = pygame.sprite.Group()

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
        positions_list = [(210, 80), (330, 80), (510, 80), (570, 80), (690, 80),
                          (210, 140), (450, 140), (570, 140),
                          (150, 200), (270, 200), (330, 200), (450, 200), (630, 200),
                          (90, 260), (210, 260), (450, 260), (690, 260),
                          (90, 320), (270, 320), (330, 320), (510, 320), (570, 320), (690, 320),
                          (210, 380), (450, 380), (570, 380),
                          (150, 440), (210, 440), (330, 440), (450, 440), (630, 440), (690, 440),
                          (90, 500), (330, 500), (570, 500),
                          (90, 560), (210, 560), (390, 560), (510, 560), (570, 560)]
        for position in positions_list:
            self.set_of_box.add(component.Box.Box(boxIMG, position, animation_hander_box))

    def draw(self, surface):
        self.set_of_block.draw(surface)
        self.set_of_box.draw(surface)
        self.set_of_bomb.draw(surface)
        self.set_of_explosion.draw(surface)

    def add_bomb(self, bomb):
        if not pygame.sprite.spritecollide(bomb, self.set_of_bomb, False):
            self.set_of_bomb.add(bomb)
            print("tak")
            return True
        else:
            print("nope")
            return False

    def add_explosions(self, explosionIMG, range, position):
        new_position = self._calculate_position_for_explosion(position)
        a, b = new_position
        step = 70
        print(position)
        self.set_of_explosion.add(component.Explosion.Explosion(explosionIMG, new_position))
        a += step
        while a - new_position[0] < range:
            explosion = component.Explosion.Explosion(explosionIMG, (a, new_position[1]))
            if pygame.sprite.spritecollide(explosion, self.set_of_block, False):
                break
            elif pygame.sprite.spritecollide(explosion, self.set_of_box, True):
                break
            else:
                self.set_of_explosion.add(explosion)
            a += step
        a = new_position[0] - step
        while a - new_position[0] > range * -1:
            explosion = component.Explosion.Explosion(explosionIMG, (a, new_position[1]))
            if pygame.sprite.spritecollide(explosion, self.set_of_block, False):
                break
            elif pygame.sprite.spritecollide(explosion, self.set_of_box, True):
                break
            else:
                self.set_of_explosion.add(explosion)
            a -= step
        b += step
        while b - new_position[1] < range:
            explosion = component.Explosion.Explosion(explosionIMG, (new_position[0], b))
            if pygame.sprite.spritecollide(explosion, self.set_of_block, False):
                break
            elif pygame.sprite.spritecollide(explosion, self.set_of_box, True):
                break
            else:
                self.set_of_explosion.add(explosion)
            b += step
        b = new_position[1] - step
        while b - new_position[1] > range * -1:
            explosion = component.Explosion.Explosion(explosionIMG, (new_position[0], b))
            if pygame.sprite.spritecollide(explosion, self.set_of_block, False):
                break
            elif pygame.sprite.spritecollide(explosion, self.set_of_box, True):
                break
            else:
                self.set_of_explosion.add(explosion)
            b -= step

    def _calculate_position_for_explosion(self, position):
        x = (position[0] // 60) * 60 + 30
        y = (position[1] // 60) * 60 + 30
        print(x, y)
        return x, y
